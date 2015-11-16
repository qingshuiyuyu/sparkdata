source  /home/hadoop/.bashrc

#eg: sh /mnt/pzz/workspace/sparkdata/pzz/sh/cmt_inc_insert.sh /data/develop/ec/tb/cmt_dbfeedid.20151103/part* /commit/comments/*2015-11-05 /data/develop/ec/tb/cmt_allfeedid.20151105 /data/develop/ec/tb/cmt_newfeedid.20151105 /data/develop/ec/tb/cmt_tmpdata.20151105

feed_dir=/data/develop/ec/tb/cmt/feedid
data_dir=/data/develop/ec/tb/cmt/tmpdata
commit_dir=/commit/comments

#输入数据
mission_data=$1
#任务id
mission_id=$2
#上次任务id
lastmission_id=$3

#获取输入参数
all_feed_input=${feed_dir}/cmt_allfeedid.${lastmission_id}
new_data_input=$1
all_feed_output=${feed_dir}/cmt_allfeedid.${mission_id}
new_feed_output=${feed_dir}/cmt_newfeedid.${mission_id}
tmp_data=${data_dir}/cmt_inc_data.${mission_id}

echo "Mission start at:"
date
echo "check argvs: "
echo "\tdata location:\t"${new_data_input}
echo "\tlast all feedid location\t"${all_feed_input}
echo "\tall feedid location\t"${all_feed_output}
echo "\tnew feedid location\t"${new_feed_output}

#处理数据
echo "Start spark job."
hadoop fs -rmr $all_feed_output
hadoop fs -rmr $new_feed_output
hadoop fs -rmr $tmp_data
spark-submit --executor-memory 20g --driver-memory 20g --total-executor-cores 105 /mnt/pzz/workspace/sparkdata/pzz/cmt/cmt_inc_clean.py -gen_data_inc ${all_feed_input}/part* $new_data_input $all_feed_output $new_feed_output $tmp_data
echo "spark job finished."

#hive 入库
echo "cp result data for test.."$tmp_data" to "${tmp_data}.test
hadoop fs -rmr ${tmp_data}.test
hadoop fs -cp $tmp_data ${tmp_data}.test

echo "insert hive"
sh  /mnt/pzz/workspace/sparkdata/pzz/sh/feed.Dynamic_partitions.sql ${tmp_data}.test

echo "completed insertting "$tmp_data

#反馈商品评论增量
echo "feed back item feed inc number to commit.."
hadoop fs -rmr /commit_feedbck/cmt/cmt_newfeedid.${mission_id}
hadoop fs -cp $new_feed_output /commit_feedbck/cmt/

echo "mission FINISH!"
date