CREATE TABLE  if not exists wl_base.t_base_phone_huangye88_userinfo_v1(
phone String COMMENT '区号+电话号码',
acode string comment '区号',
phone_num string comment '电话号码',
company String COMMENT '公司名称',
auth String COMMENT '授权',
sex String COMMENT '性别',
birth_day String COMMENT '出生日期',
jifen String COMMENT '积分',
row String COMMENT '介绍',
name String COMMENT '名字',
area String COMMENT '地点',
register_time String COMMENT '注册时间',
last_log_in String COMMENT '上次登录时间'
)
COMMENT '黄页88用户信息'
PARTITIONED BY  (ds STRING )
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' stored as textfile;

load data inpath '/user/lel/temp/huangye88_userinfo_1/' into table t_base_phone_huangye88_userinfo_v1 partition(ds = 20170409)
