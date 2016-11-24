#coding:utf-8
__author__ = 'wrt'
import sys
import rapidjson as json
from pyspark import SparkContext
from pyspark.sql import *

sc = SparkContext(appName="rong360_features_hebing")
sqlContext = SQLContext(sc)
hiveContext = HiveContext(sc)


def valid_jsontxt(content):
    # res = content
    if type(content) == type(u""):
        res = content.encode("utf-8")
    else:
        res = str(content)
    return res.replace('\n',"").replace("\r","").replace('\001',"").replace("\u0001","")


def feature_main(line):
    ss = line.strip().split("\001")
    # a = len(ss)
    tel = ss[0]
    result = ss[1:]
    return (tel,result)


def f_3j_reindex(line):
    ss = line.strip().split("\001")
    # user_id = ss[0]
    features = ss[1].split(" ")
    return [(valid_jsontxt(i.split(':')[0]),"") for i in features]

# a = 34
# a_list = [0]*1000000

def feature_3j(line,fea_3j):
    ss = line.strip().split("\001")
    tel = ss[0]
    features = ss[1].split(" ")
    f_map = {}
    result = []
    for feature in features:
        ff = feature.split(":")
        f_value = ff[0]
        v_value = ff[1]
        f_index = fea_3j.index(f_value)
        f_map[f_index] = v_value
    for i in range(len(fea_3j)):
        if f_map.has_key(i):
            result.append(f_map[i])
        else:
            result.append("0.0")
    return (tel,result)

def hebing(x,y):
    # lv = []
    result = []
    if len(y) != 2:
        return None
    else:
        if len(y[0]) < len(y[1]):
            lv = y[0] + y[1]
        else:
            lv = y[1] + y[0]
    result.append(x)
    for i in range(len(lv)):
        result.append(str(i) + ":" + str(lv[i]))
    return " ".join([valid_jsontxt(ln) for ln in result])


def hebing_2(x,y):
    result = []
    result.append(x)
    lv = y[0] + y[1]
    for i in range(len(lv)):
        result.append(str(i) + ":" + str(lv[i]))
    return " ".join([valid_jsontxt(ln) for ln in result])


s_3j = "/hive/warehouse/wlservice.db/t_zlj_tmp_rong360_1w_record_level3_feature/*"
s_main = "/hive/warehouse/wlservice.db/t_rong360_model_features_new/000000_0"


rdd_fea_3j = sc.textFile(s_3j).flatMap(lambda x:f_3j_reindex(x)).groupByKey().mapValues(list).map(lambda (x, y): x)
fea_3j = list(rdd_fea_3j.collect())
rdd_3j = sc.textFile(s_3j).map(lambda x:feature_3j(x,fea_3j))
rdd_fea_main = hiveContext.sql('desc wlservice.t_rong360_model_features_new')
rdd_main = sc.textFile(s_main).map(lambda x:feature_main(x))
# rdd = rdd_main.union(rdd_3j).groupByKey().mapValues(list).map(lambda (x, y): hebing(x,y)).filter(lambda x:x!=None)
rdd = rdd_main.join(rdd_3j).map(lambda (x,y):hebing_2(x,y))
rdd.saveAsTextFile('/user/wrt/temp/rong360_tel_features')

fea_main = [valid_jsontxt(ln.col_name) for ln in rdd_fea_main.collect()]
fea_all = fea_main + fea_3j
sc.parallelize(fea_all).saveAsTextFile('/user/wrt/temp/rong360_features_name')



#hfs -rmr /user/wrt/temp/rong360_tel_features
#hfs -rmr /user/wrt/temp/rong360_3j_features
#spark-submit  --executor-memory 9G  --driver-memory 9G  --total-executor-cores 120 rong360_features_hebing.py