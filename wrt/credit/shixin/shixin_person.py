#coding:utf-8
__author__ = 'wrt'
import sys
import rapidjson as json
from pyspark import SparkContext

sc = SparkContext(appName="shixin_person")

def valid_jsontxt(content):
    res = content
    if type(content) == type(u""):
        res = content.encode("utf-8")
    # return res.replace("\\n", " ").replace("\n"," ").replace("\u0001"," ").replace("\001", "").replace("\\r", "")
    return res.replace('\n',"").replace("\r","").replace('\001',"").replace("\u0001","")


def f1(line):
    ob = json.loads(valid_jsontxt(line.strip()))
    if type(ob) != type({}): return None
    id = str(ob.get("id","-"))
    iname = ob.get("iname","-")
    casecode = ob.get("caseCode","-")
    cardnum = ob.get("cardNum","-")
    age = str(ob.get("age","-"))
    sexy = ob.get("sexy","-")
    businessentity = ob.get("businessEntity","-")
    courtname = ob.get("courtName","-")
    areaname = ob.get("areaName","-")
    partytypename = ob.get("partyTypeName","-")
    gistid = ob.get("gistId","-")
    regdate = ob.get("regDate","-")
    gistunit = ob.get("gistUnit","-")
    duty = ob.get("duty","-")
    performance = ob.get("performance","-")
    disrupttypename = ob.get("disruptTypeName","-")
    publishdate = ob.get("publishDate","-")
    performedpart = ob.get("performedPart","-")
    unperformpart = ob.get("unperformPart","-")
    result = []
    result.append(id)
    result.append(iname)
    result.append(casecode)
    result.append(cardnum)
    result.append(age)
    result.append(sexy)
    result.append(businessentity)
    result.append(courtname)
    result.append(areaname)
    result.append(partytypename)
    result.append(gistid)
    result.append(regdate)
    result.append(gistunit)
    result.append(duty)
    result.append(performance)
    result.append(disrupttypename)
    result.append(publishdate)
    result.append(performedpart)
    result.append(unperformpart)
    return (id,result)
#
# def f2(line):
#


# rdd_c = sc.textFile("/commit/shixin.info.20161029.json").map(lambda x:f(x))
# last_day = "20161029"
now_day = "20161205"

rdd_c = sc.textFile("/commit/credit/shixin/shixin.info.person." + now_day).map(lambda x:f1(x)).filter(lambda x:x!=None)
rdd_now = rdd_c.groupByKey().mapValues(list).map(lambda (x,y):"\001".join([valid_jsontxt(i) for i in y[0]]))
# rdd_last = sc.textFile("/hive/warehouse/wlcredit.db/t_wrt_shixin_person/" + last_day).map(lambda x:f2(x))
rdd_now.saveAsTextFile("/user/wrt/temp/shixin_personinfo")

# hfs -rmr /user/wrt/temp/shixin_personinfo
# spark-submit  --executor-memory 6G  --driver-memory 8G  --total-executor-cores 80 shixin_person.py
# LOAD DATA  INPATH '/user/wrt/temp/shixin_info_20161029' OVERWRITE INTO TABLE t_wrt_shixin_person PARTITION (ds='20161029');
# LOAD DATA  INPATH '/user/wrt/temp/shixin_info_20161029' OVERWRITE INTO TABLE t_wrt_shixin_person PARTITION (ds='temp');