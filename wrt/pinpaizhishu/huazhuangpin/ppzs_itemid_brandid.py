#coding:utf-8
__author__ = 'wrt'
import sys
import rapidjson as json
from pyspark import SparkContext

sc = SparkContext(appName="ppzs_itemid_brandid")

def valid_jsontxt(content):
    # res = content
    if type(content) == type(u""):
        res = content.encode("utf-8")
    else:
        res = str(content)
    return res.replace('\n',"").replace("\r","").replace('\001',"").replace("\u0001","")

def get_brand(line):
    brand_id = line.strip()
    return (brand_id,"1")

def get_cate_dict(line):
    ss = line.strip().split("\001")
    return (ss[0],[ss[1],ss[3],ss[8]])


def f(line,brand_dict,cate_dict):
    ss = line.strip().split("\t")
    if len(ss) != 3: return None
    item_id = ss[1]
    itemInfoModel = data.get('itemInfoModel',"-")
    categoryId = itemInfoModel.get('categoryId','-')
    root_cat_id = cate_dict.get(categoryId,["-","-","-"])[1]
    if not root_cat_id in ["50010788","1801"]: return None #不属于纸尿裤的直接舍弃掉
    txt = valid_jsontxt(ss[2])
    ob = json.loads(txt)
    if type(ob) != type({}): return None
    data = ob.get('data',"-")
    if data == "-": return None
    trackParams = data.get('trackParams',{})
    brandId = valid_jsontxt(trackParams.get('brandId','-'))
    # if brandId == "-": return None
    if not brand_dict.has_key(brandId): return None
    return (item_id,brandId)


b_dim = "/hive/warehouse/wlservice.db/t_wrt_tmp_ppzs_brandid"
s = "/commit/tb_tmp/iteminfo/20161107.pinpai.iteminfo.complete"
c_dim = "/hive/warehouse/wlbase_dev.db/t_base_ec_dim/ds=20151023/1073988839"
brand_dict = sc.broadcast(sc.textFile(b_dim).map(lambda x: get_brand(x)).filter(lambda x:x!=None).collectAsMap()).value
cate_dict = sc.broadcast(sc.textFile(c_dim).map(lambda x: get_cate_dict(x)).filter(lambda x:x!=None).collectAsMap()).value
rdd = sc.textFile(s).map(lambda x:f(x,brand_dict,cate_dict)).filter(lambda x:x!=None)
rdd.groupByKey().mapValues(list).map(lambda (x,y):valid_jsontxt(x) + "\001" + valid_jsontxt(y[0]))\
    .saveAsTextFile("/user/wrt/temp/ppzs_itemid_brandid")


# 所得item_id为店铺中的item_id，包括各种品牌，后续需要过滤掉非目标品牌
# hfs -rmr /user/wrt/temp/ppzs_itemid_brandid
# spark-submit  --executor-memory 6G  --driver-memory 8G  --total-executor-cores 80  ppzs_itemid_brandid.py
# LOAD DATA  INPATH '/user/wrt/temp/ppzs_itemid_brandid' OVERWRITE INTO TABLE ppzs_itemid_brandid PARTITION (ds='20161108');