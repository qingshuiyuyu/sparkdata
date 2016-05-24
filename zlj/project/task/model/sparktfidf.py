# coding:utf-8
__author__ = 'zlj'
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.types import *
import time
import rapidjson as json



from pyspark import SparkContext
from pyspark.mllib.feature import IDF
from  pyspark.mllib.linalg import *
from collections import Counter

sc = SparkContext(appName="cmt")
sqlContext = SQLContext(sc)
hiveContext = HiveContext(sc)

path = '/user/zlj/nlp/t_zlj_item_title/part-00000'

# doc = sc.textFile(path).map(lambda line: line.split('\001')).map(lambda x: (x[0], x[1].split() + [x[0] + '_doc']))

docs= sc.textFile(path).map(lambda x:x.split('\001')).map(lambda x:([x[0]],x[1].split())).repartition(100)

# docs=docs_index.map(lambda x:x[0][1].split())

words=docs.map(lambda x:x[1]).flatMap(lambda x:x).distinct().collect()

words_bc=sc.broadcast(words).value
word_index={}
index_word={}
for i ,w in enumerate(words_bc):
    word_index[w]=i
    index_word[i]=w

word_index_bc=sc.broadcast(word_index).value
index_word_bc=sc.broadcast(index_word).value

size=len(words_bc)
def count(v,doc_id):
    dict= sorted(Counter(v).iteritems(), key=lambda d:d[0])
    return Vectors.sparse(size,[i[0] for i in dict ]+[int(doc_id)],[i[1] for i in dict ]+[1])
tf=docs.map(lambda x:count([word_index_bc[i] for i in x[1]],x[0]))
tf.cache()
idf = IDF(minDocFreq=1).fit(tf)
tfidf = idf.transform(tf)
tfidf.repartition(20).map(lambda x:'\t'.join(['_'.join([index_word_bc[i],str(w)]) for  i ,w in zip(x.indices,x.values)])).\
    filter(lambda x:len(x)>2).saveAsTextFile('/user/zlj/nlp/t_zlj_item_title_tfidf')




