



create table t_zlj_qq_find_qq_school  as
select
t2.qq_id ,
t1.find_schools
from
(
select
*
from qq_group_info where ds='school'

 )t1

 join
qun_member_info t2 on t1.qun_id=t2.qun_id
;


select COUNT(DISTINCT qq_id ) from t_zlj_qq_find_qq_school ;



create table t_zlj_qq_tmp as
SELECT

 t1.*,t2.qun_id
FROM t_zlj_qq_find_qq_school t1 JOIN

 (
  SELECT t4.*
  FROM
   qun_member_info t4 LEFT JOIN
   (
    SELECT *
    FROM qq_group_info
    WHERE ds = 'school'
   ) t3 ON t3.qun_id = t4.qun_id
  WHERE t3.qun_id IS NULL

 ) t2 ON t1.qq_id = t2.qq_id;



create table t_zlj_qq_tmp_find_qq_school_zhuanye  as
select

 t1.qun_id,
 title,
 qun_text,
t1.find_schools
from
(
select * from qq_group_info where ds='zhuanye'

 )t1

 join
 (
  select qun_id
   from
t_zlj_qq_tmp
  group by qun_id
)t2 on t1.qun_id=t2.qun_id
;



create table t_zlj_qq_tmp_find_qq_school_zhuanye_count  as

 SELECT
 qun_id,
 max(title) ,
 max(qun_text),
 max(find_schools),
  count(1) as num

 from (
  select
 t1.qun_id,
 t1.title ,
 t1.qun_text,
 t1.find_schools
from
(
select * from qq_group_info where ds='zhuanye'

 )t1

 join

t_zlj_qq_tmp
t2
 on t1.qun_id=t2.qun_id

 )tt

 group by qun_id
;





# create table t_zlj_qq_find_qq_school  as


# 24539245
 SELECT count(DISTINCT qq_id)
 FROM
 (select
t2.qq_id
from
t_zlj_qq_tmp_find_qq_school_zhuanye_count  t1

 join
qun_member_info t2 on t1.qun_id=t2.qun_id and t1.num >4

 UNION  all
    select qq_id from t_zlj_qq_find_qq_school
 )t
;