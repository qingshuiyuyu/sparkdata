#!/usr/bin/env bash
ds=$1

/home/hadoop/hive/bin/hive<<EOF

use wlbase_dev;

LOAD DATA  INPATH '/user/wrt/daysale_tmp' OVERWRITE INTO TABLE t_base_ec_item_sale_dev PARTITION (ds='$ds');

EOF