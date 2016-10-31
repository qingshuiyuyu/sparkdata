#coding:utf-8
__author__ = 'wrt'
import sys
import rapidjson as json
from pyspark import SparkContext
sc = SparkContext(appName="womaiwang")




foods = ["澳洲进口牛肉",
"奇异果",
"佳沛奇异果",
"苹果",
"阿克苏苹果",
"牛排",
"阳澄湖大闸蟹",
"智利三文鱼",
"美国车厘子",
"智利车厘子",
"真鳕鱼",
"虾仁",
"北极虾",
"厄瓜多尔白虾",
"哈密瓜",
"阿根廷红虾",
"五花肉",
"牛腩",
"排骨",
"乌拉圭牛腱子",
"巴西牛腱子",
"澳洲牛腱子",
"羊排",
"羔羊肉",
"羊肉卷",
"小龙虾",
"大对虾",
"龙虾",
"牛肋条",
"牛霖肉",
"T骨牛排",
"猪排",
"牛肋条肉",
"肋条肉",
"猪肋排",
"牛眼肉",
"牛肉串",
"牛肋排",
"牛柳",
"黄花鱼",
"三都港黄花鱼",
"舟山带鱼段",
"带鱼",
"土鸡",
"德清源鸡蛋",
"赣南脐橙",
"鲑鱼",
"大洋世家大黄鱼",
"大洋世家北极虾",
"大厨小鲜小龙虾",
"蒜蓉粉丝扇贝",
"波士顿龙虾",
"小黄鱼",
"柠檬",
"鸡蛋",
"蓝莓",
"海参",
"葡萄",
"番茄",
"橙",
"香蕉",
"芒果",
"榴莲",
"桂圆",
"金枪鱼",
"梨",
"樱桃",
"西梅",
"鸡肉",
"南瓜",
"柚子",
"鱿鱼",
"山药",
"蘑菇",
"猕猴桃",
"西柚",
"石榴",
"板栗",
"黄瓜",
"糯玉米",
"紫薯",
"红提",
"扇贝",
"鸡翅",
"土豆",
"猪蹄",
"蜜柚",
"龙眼",
"香梨",
"带鱼",
"火龙果",
"荔枝",
"牛油果",
"西红柿",
"咸鸭蛋",
"橙子",
"凤梨",
"菠萝",
"木瓜",
"鱼片",
"海带",
"肥牛",
"翅中",
"鸡块",
"脆皮肠",
"鲽鱼",
"帝王蟹",
"里脊",
"西兰花",
"油菜",
"水果玉米",
"刺参",
"羔羊肉片",
"梅花肉",
"鹌鹑蛋",
"冬枣",
"尖椒",
"生菜",
"金针菇",
"大黄鱼",
"银鱼",
"羊腿",
"猪肘子",
"松花蛋",
"鸡小胸",
"鸡柳",
"桔子",
"水果萝卜",
"黄金梨",
"大葱",
"沙窝萝卜",
"红薯",
"鲳鱼",
"凤尾虾",
"虎虾",
"黄金蟹",
"羔羊排",
"后腿肉",
"猪肉馅",
"琵琶腿",
"鸡胗",
"童子鸡",
"娃娃菜",
"芹菜",
"青椒",
"冬瓜",
"墨鱼",
"大龙虾",
"青口贝",
"羊肉串",
"牛尾",
"猪肉通脊",
"鸡爪",
"山竹",
"油麦菜",
"圆白菜",
"茄子",
"秋葵",
"豇豆",
"羊前腿",
"牛肉馅",
"牛仔骨",
"小白菜",
"西葫芦",
"朝天椒",
"红鱼",
"秋刀鱼",
"羊肉片",
"羊肉馅",
"羊颈排",
"羔羊龙骨",
"肥瘦肉馅",
"猪肉后尖",
"鸡腿",
"鸡胸肉",
"百香果",
"莲雾",
"奶白菜",
"圣女果",
"豆角",
"茭白",
"菜花",
"扁豆",
"海藻丝",
"毛豆",
"鲫鱼",
"雪蟹",
"羊肝",
"羊脊骨",
"羔羊肚",
"羊后腿",
"牦牛肉",
"牛肉丸",
"牛上脑肉",
"牛三角",
"去骨小牛排",
"去皮牛尾",
"牛三角肉",
"猪大排",
"小排",
"猪小排",
"猪脚",
"鸭蛋",
"乌鸡",
"鸡肉丸",
"鸡心",
"蛇果",
"黄梨",
"乌塌菜",
"油栗",
"杭椒",
"多宝鱼",
"墨鱼仔",
"高白鲑",
"美极虾",
"虾皮",
"羊肩肉",
"羊腱",
"羊腿肉",
"羊腩",
"羊腰子",
"羊颈肉",
"羔羊肉馅",
"羊寸排",
"手把肉",
"羊肚",
"牛汤骨",
"牛脖子肉",
"前肩肉",
"里脊肉",
"猪大肠",
"猪肩肉",
"猪腔骨",
"后臀尖",
"猪腰",
"翅根",
"乳鸽",
"鸡肉串",
"盐酥鸡",
"翅尖",
"柿子",
"茼蒿",
"鸡毛菜",
"蒿子秆",
"芥蓝",
"深海鳌虾",
"红毛蟹",
"羊龙骨",
"羊棒骨",
"羊后腿卷",
"羊腰",
"羊前腿肉",
"羊前腿棒",
"去骨养肩肉",
"羊五花肉",
"羊上脑",
"羊上脑肉",
"羊霖肉",
"羊腔骨",
"羊板筋",
"羊菲力",
"羊腩肉",
"牛里脊",
"牛肋骨",
"牛小排",
"牛角砧",
"牛三角肩肉",
"猪后尖",
"猪舌",
"猪前排",
"猪展肉",
"猪尖肉",
"雪花肉",
"猪肾",
"猪耳朵",
"猪耳",
"猪前腿肉",
"猪后腿肉",
"猪肉汤骨",
"鸡肉丁",
"贻贝",
"梭子蟹"]

def valid_jsontxt(content):
    res = content
    if type(content) == type(u""):
        res = content.encode("utf-8")
    # return res.replace("\\n", " ").replace("\n"," ").replace("\u0001"," ").replace("\001", "").replace("\\r", "")
    return res.replace('\n',"").replace("\r","").replace('\001',"").replace("\u0001","")

def f(line,foods):
    ss = line.strip().split("\001")
    user_id = valid_jsontxt(ss[2])
    title = valid_jsontxt(ss[8])
    for ln in foods:
        if ln in title:
            # return valid_jsontxt(ln) + "\001" + valid_jsontxt(user_id)
            return (ln,user_id)
    return None

def quchong(x,y):
    num = str(len(set(y)))
    return valid_jsontxt(x) + "\001" + valid_jsontxt(num)

rdd = sc.textFile("/hive/warehouse/wlbase_dev.db/t_base_ec_record_dev_new/ds=true")
rdd_r = rdd.map(lambda x:f(x,foods)).filter(lambda x:x!=None).groupByKey().mapValues(list).map(lambda (x,y):quchong(x,y))
rdd_r.saveAsTextFile("/user/wrt/temp/womaiwang_tongji")
# spark-submit  --executor-memory 9G  --driver-memory 8G  --total-executor-cores 120  womaiwang.py