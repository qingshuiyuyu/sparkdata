
CREATE  TABLE  if not exists t_base_weibo_usertag (

id bigint COMMENT ' 用户UID ' ,

tags string COMMENT '标签'
)
COMMENT '微博用户标签'
PARTITIONED BY  (ds STRING )
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'   LINES TERMINATED BY '\n'
stored as textfile ;