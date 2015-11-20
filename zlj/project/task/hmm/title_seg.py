# encoding: utf-8
__author__ = 'zlj'

from pyspark import SparkContext
from pyspark.sql import *

sc = SparkContext(appName="seg")
sqlContext = SQLContext(sc)
from pyspark.sql.types import *

hiveContext = HiveContext(sc)

import jieba.posseg as pseg



# jieba.load_userdict('./dict/userdict')


schema1 = StructType([
    StructField("item_id", StringType(), True),
    StructField("root_cat_id", StringType(), True),
    StructField("root_cat_name", StringType(), True),
    StructField("title", StringType(), True),
    StructField("title_cut", StringType(), True),
    StructField("title_seg", StringType(), True)
   ])
def valid_jsontxt(content):
    if type(content) == type(u""):
        return content.encode("utf-8")
    else :
        return content
def seg(x):
    title=x.title
    if title is None:
        return None
    lv1=[]
    lv2=[]
    for word,tag in pseg.cut(valid_jsontxt(title).strip()):
        lv1.append(valid_jsontxt(word))
        lv2.append(valid_jsontxt(word)+"@_@"+valid_jsontxt(tag))
    return [x.item_id,x.root_cat_id,x.root_cat_name,x.title].append([' '.join(lv1),' '.join(lv2)])



hiveContext.sql('use wlbase_dev')


sql='''

select
item_id,root_cat_id,root_cat_name,title
from
t_base_ec_item_dev
where ds=20151112

'''

df=hiveContext.sql(sql)
rdd=df.map(lambda x:seg(x)).filter(lambda x: x is not None)

df1=hiveContext.createDataFrame(rdd,schema1)

hiveContext.registerDataFrameAsTable(df1,'tmptable')

hiveContext.sql('drop table if exists t_zlj_corpus_item_seg')
hiveContext.sql('create table  t_zlj_corpus_item_seg  as select * from tmptable')

