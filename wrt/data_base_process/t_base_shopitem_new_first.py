#coding:utf-8
__author__ = 'wrt'

import sys
import rapidjson as json
from pyspark import SparkContext
sc = SparkContext(appName="t_base_shopitem")

def valid_jsontxt(content):
    # res = content
    if type(content) == type(u""):
        res = content.encode("utf-8")
    else:
        res = str(content)
    return res.replace('\n',"").replace("\r","").replace('\001',"").replace("\u0001","")

def f1(line):
    ss = line.strip().split("\t",4)
    shop_id = ss[1]
    ts = ss[0]
    text = ss[4]
    if text == "noshop": return [None]
    ob = json.loads(valid_jsontxt(text))
    if type(ob) != type([]): return [None]
    result = []
    for item in ob:
        lv = []
        item_id = item.get("item_id","-")
        title = item.get("title","-")
        picUrl = item.get("picUrl","-")
        sold = item.get("sold","-")
        # day_sold = '0' #日销量，默认为0
        reservePrice = item.get("reservePrice","-")
        if reservePrice == "": reservePrice = "-"
        salePrice = item.get("salePrice","-")
        # auctionType = item.get("auctionType","-")
        up_day = "20160819"
        down_day = "0"
        lv.append(valid_jsontxt(shop_id))
        # lv.append(valid_jsontxt(shopTitle))
        # lv.append(valid_jsontxt(item_count))
        lv.append(valid_jsontxt(item_id))
        lv.append(valid_jsontxt(title))
        lv.append(valid_jsontxt(picUrl))
        lv.append(valid_jsontxt(sold))
        # lv.append(valid_jsontxt(day_sold))
        lv.append(valid_jsontxt(reservePrice))
        lv.append(valid_jsontxt(salePrice))
        # lv.append(valid_jsontxt(auctionType))
        # lv.append(valid_jsontxt(quantity))
        # lv.append(valid_jsontxt(totalSoldQuantity))
        # lv.append(valid_jsontxt(orderCost))
        # lv.append(valid_jsontxt(bonusAmount))
        # lv.append(valid_jsontxt(onSale))
        lv.append(valid_jsontxt(up_day)) #上架日期
        lv.append(valid_jsontxt(down_day)) #0代表上架，日期代表下架日期
        lv.append(valid_jsontxt(ts))
        result.append((item_id,lv))
    return result

def quchong(x,y):
    max = 0
    item_list = y
    for ln in item_list:
        if int(ln[-1]) > max:
            max = int(ln[-1])
            y = ln
    return "\001".join(y)


s = "/commit/shopitem/20160819/*"
rdd1_c = sc.textFile(s).flatMap(lambda x:f(x)).filter(lambda x:x != None)
rdd1 = rdd1_c.groupByKey().mapValues(list).map(lambda (x, y):quchong(x, y))
rdd1.saveAsTextFile('/user/wrt/shopitem_tmp')

# hfs -rmr /user/wrt/shopitem_tmp
# spark-submit  --executor-memory 6G  --driver-memory 8G  --total-executor-cores 80 t_base_shopitem_first.py
#LOAD DATA  INPATH '/user/wrt/shopitem_tmp' OVERWRITE INTO TABLE t_base_ec_shopitem_dev PARTITION (ds='20160721');