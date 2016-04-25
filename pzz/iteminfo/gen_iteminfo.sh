source ~/.bashrc

#eg:sh gen_iteminfo.sh -geninc /commit/iteminfo/2016041[5-9] /hive/warehouse/wlbase_dev.db/t_base_ec_item_house /hive/warehouse/wlbase_dev.db/t_base_ec_item_house_merge_tmp

workspace_path=/home/yarn/pzz/workspace/sparkdata/pzz
echo "\targv[1]:-genbase, 形成基础仓库.  argv[2]:inputpath   argv[3]:outputpath\n
    \targv[1]:-geninc, 每日新增数据.  argv[2]:input data path   argv[3]:input base path  argv[4]:outputpath"
spark_midlle $workspace_path/xzx/gen_iteminfo.py $1 $2 $3 $4
