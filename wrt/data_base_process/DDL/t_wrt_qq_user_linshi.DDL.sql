use wlbase_dev;

CREATE EXTERNAL TABLE  if not exists t_wrt_qq_user_linshi (
uin  STRING   COMMENT 'qq号' ,
birthday STRING COMMENT 'yyyy-mm-dd',
phone  STRING COMMENT '手机号，自己填写，内容可能失真' ,
gender_id  BIGINT COMMENT '性别 1：男  2：女' ,
college  STRING   COMMENT '学校' ,
lnick  STRING COMMENT '个人签名' ,
loc_id STRING COMMENT '所在地编码' ,
loc STRING COMMENT '所在地',
h_loc_id STRING COMMENT '家乡编码',
h_loc STRING COMMENT '家乡地',
personal  STRING   COMMENT '个人说明' ,
shengxiao  STRING COMMENT '生肖' ,
gender  BIGINT COMMENT '性别  1：男  2：女' ,
occupation  STRING  COMMENT '职位' ,
constel  STRING COMMENT '星座' ,
blood  STRING COMMENT '血型' ,
url  STRING   COMMENT '头像' ,
homepage  STRING COMMENT '主页' ,
nick  STRING COMMENT '昵称' ,
email  STRING  COMMENT 'email' ,
uin2  STRING   COMMENT '登陆邮箱账号' ,
mobile  STRING COMMENT '有的话部分加密139********',
ts STRING COMMENT '采集时间戳',
age  INT
)
COMMENT 'qq用户信息'
PARTITIONED BY  (ds STRING )
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'   LINES TERMINATED BY '\n' ;