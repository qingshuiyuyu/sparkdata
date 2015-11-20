__author__ = 'wrt'

#coding:utf-8
import sys
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.types import *
sc = SparkContext(appName="spark item_sale")
sqlContext = SQLContext(sc)
hiveContext = HiveContext(sc)
def quchong(x):
    max = 0
    item_list = x[1:]
    if len(item_list) == 1:
        item_list[9] = 1 #flag为1,该总销量为复制前一天信息
    else:
        for ln in item_list:
            if int(ln[8]) > max:
                max = int(ln[8])
                x[1] = item_list
    return x

schema = StructType([
    StructField("item_id",StringType(), True),
	StructField("item_title",StringType(), True),
	StructField("r_price",FloatType(), True),
    StructField("s_price",FloatType(), True),
    StructField("bc_type",StringType(), True),
    StructField("quantity",IntegerType(), True),
    StructField("total_sold",IntegerType(), True),
    StructField("order_cost",IntegerType(), True),
    StructField("shop_id",StringType(), True),
    StructField("ts",StringType(), True)
	])

hiveContext.sql('use testhive')
s1 = sys.argv[1] #today
s2 = sys.argv[2] #yesterday
rdd1 = sc.textFile(s1).filter(lambda x:x!=None).map(lambda x:(x[0],x[1:]))
rdd2 = sc.textFile(s2).filter(lambda x:x!=None).map(lambda x:(x[0],x[1:]))
rdd = rdd1.union(rdd2).groupByKey().map(lambda x:quchong(x)).map(lambda x:[x[0]] + x[1:])
df = hiveContext.createDataFrame(rdd, schema)
hiveContext.registerDataFrameAsTable(df, 'data')
#st = s.find('2015')
#ds2 = s[st:st+4] + s[st+5:st+7] + s[st+8:st+10]
l = len(s1)
ds1 = s1[l-8:]
hiveContext.sql('insert overwrite table t_base_ec_item_sale_dev PARTITION(ds=' + ds1 + ') select * from data')
		#.saveAsTextFile("/user/wrt/item_sale")
sc.stop()
#spark-submit  --executor-memory 4G  --driver-memory 20G  --total-executor-cores 80 t_wrt_base_ec_item_sale.py
#/commit/shopitem/20151116/*6