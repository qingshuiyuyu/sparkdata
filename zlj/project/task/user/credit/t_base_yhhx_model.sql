
create table t_base_yhhx_model_tel as
select * from
(SELECT
 uid  as tel ,
buy_month              ,
avg_cnt                ,
std_cnt                ,
avg_price              ,
std_price              ,
avg_price_ratio        ,
cnt_ratio_11           ,
cnt_ratio_1101         ,
cnt_ratio_1201         ,
cnt_ratio_120886001    ,
cnt_ratio_120950002    ,
cnt_ratio_121266001    ,
cnt_ratio_121536003    ,
cnt_ratio_121536007    ,
cnt_ratio_122650005    ,
cnt_ratio_122684003    ,
cnt_ratio_122718004    ,
cnt_ratio_122852001    ,
cnt_ratio_122928002    ,
cnt_ratio_122950001    ,
cnt_ratio_122952001    ,
cnt_ratio_124024001    ,
cnt_ratio_124044001    ,
cnt_ratio_124050001    ,
cnt_ratio_124242008    ,
cnt_ratio_124354002    ,
cnt_ratio_124458005    ,
cnt_ratio_124466001    ,
cnt_ratio_124468001    ,
cnt_ratio_124470001    ,
cnt_ratio_124484008    ,
cnt_ratio_124750013    ,
cnt_ratio_14           ,
cnt_ratio_1512         ,
cnt_ratio_16           ,
cnt_ratio_1625         ,
cnt_ratio_1801         ,
cnt_ratio_20           ,
cnt_ratio_21           ,
cnt_ratio_23           ,
cnt_ratio_25           ,
cnt_ratio_26           ,
cnt_ratio_27           ,
cnt_ratio_28           ,
cnt_ratio_2813         ,
cnt_ratio_29           ,
cnt_ratio_30           ,
cnt_ratio_33           ,
cnt_ratio_34           ,
cnt_ratio_35           ,
cnt_ratio_40           ,
cnt_ratio_50002766     ,
cnt_ratio_50002768     ,
cnt_ratio_50004958     ,
cnt_ratio_50006842     ,
cnt_ratio_50006843     ,
cnt_ratio_50007216     ,
cnt_ratio_50007218     ,
cnt_ratio_50008075     ,
cnt_ratio_50008090     ,
cnt_ratio_50008141     ,
cnt_ratio_50008163     ,
cnt_ratio_50008164     ,
cnt_ratio_50008165     ,
cnt_ratio_50008907     ,
cnt_ratio_50010404     ,
cnt_ratio_50010728     ,
cnt_ratio_50010788     ,
cnt_ratio_50011397     ,
cnt_ratio_50011665     ,
cnt_ratio_50011699     ,
cnt_ratio_50011740     ,
cnt_ratio_50011949     ,
cnt_ratio_50011972     ,
cnt_ratio_50012029     ,
cnt_ratio_50012082     ,
cnt_ratio_50012100     ,
cnt_ratio_50012164     ,
cnt_ratio_50013864     ,
cnt_ratio_50013886     ,
cnt_ratio_50014811     ,
cnt_ratio_50014812     ,
cnt_ratio_50014927     ,
cnt_ratio_50016348     ,
cnt_ratio_50016349     ,
cnt_ratio_50016422     ,
cnt_ratio_50016891     ,
cnt_ratio_50017300     ,
cnt_ratio_50018004     ,
cnt_ratio_50018222     ,
cnt_ratio_50018264     ,
cnt_ratio_50019095     ,
cnt_ratio_50019780     ,
cnt_ratio_50020275     ,
cnt_ratio_50020332     ,
cnt_ratio_50020485     ,
cnt_ratio_50020579     ,
cnt_ratio_50020611     ,
cnt_ratio_50020808     ,
cnt_ratio_50020857     ,
cnt_ratio_50022517     ,
cnt_ratio_50022703     ,
cnt_ratio_50023282     ,
cnt_ratio_50023575     ,
cnt_ratio_50023717     ,
cnt_ratio_50023722     ,
cnt_ratio_50023724     ,
cnt_ratio_50023804     ,
cnt_ratio_50023878     ,
cnt_ratio_50023904     ,
cnt_ratio_50024451     ,
cnt_ratio_50024612     ,
cnt_ratio_50024971     ,
cnt_ratio_50025004     ,
cnt_ratio_50025110     ,
cnt_ratio_50025111     ,
cnt_ratio_50025705     ,
cnt_ratio_50025707     ,
cnt_ratio_50026316     ,
cnt_ratio_50026523     ,
cnt_ratio_50026555     ,
cnt_ratio_50026800     ,
cnt_ratio_50050359     ,
cnt_ratio_50050471     ,
cnt_ratio_50074001     ,
cnt_ratio_50158001     ,
cnt_ratio_50454031     ,
cnt_ratio_50468001     ,
cnt_ratio_50510002     ,
cnt_ratio_99           ,
price_ratio_11         ,
price_ratio_1101       ,
price_ratio_1201       ,
price_ratio_120886001  ,
price_ratio_120950002  ,
price_ratio_121266001  ,
price_ratio_121536003  ,
price_ratio_121536007  ,
price_ratio_122650005  ,
price_ratio_122684003  ,
price_ratio_122718004  ,
price_ratio_122852001  ,
price_ratio_122928002  ,
price_ratio_122950001  ,
price_ratio_122952001  ,
price_ratio_124024001  ,
price_ratio_124044001  ,
price_ratio_124050001  ,
price_ratio_124242008  ,
price_ratio_124354002  ,
price_ratio_124458005  ,
price_ratio_124466001  ,
price_ratio_124468001  ,
price_ratio_124470001  ,
price_ratio_124484008  ,
price_ratio_124750013  ,
price_ratio_14         ,
price_ratio_1512       ,
price_ratio_16         ,
price_ratio_1625       ,
price_ratio_1801       ,
price_ratio_20         ,
price_ratio_21         ,
price_ratio_23         ,
price_ratio_25         ,
price_ratio_26         ,
price_ratio_27         ,
price_ratio_28         ,
price_ratio_2813       ,
price_ratio_29         ,
price_ratio_30         ,
price_ratio_33         ,
price_ratio_34         ,
price_ratio_35         ,
price_ratio_40         ,
price_ratio_50002766   ,
price_ratio_50002768   ,
price_ratio_50004958   ,
price_ratio_50006842   ,
price_ratio_50006843   ,
price_ratio_50007216   ,
price_ratio_50007218   ,
price_ratio_50008075   ,
price_ratio_50008090   ,
price_ratio_50008141   ,
price_ratio_50008163   ,
price_ratio_50008164   ,
price_ratio_50008165   ,
price_ratio_50008907   ,
price_ratio_50010404   ,
price_ratio_50010728   ,
price_ratio_50010788   ,
price_ratio_50011397   ,
price_ratio_50011665   ,
price_ratio_50011699   ,
price_ratio_50011740   ,
price_ratio_50011949   ,
price_ratio_50011972   ,
price_ratio_50012029   ,
price_ratio_50012082   ,
price_ratio_50012100   ,
price_ratio_50012164   ,
price_ratio_50013864   ,
price_ratio_50013886   ,
price_ratio_50014811   ,
price_ratio_50014812   ,
price_ratio_50014927   ,
price_ratio_50016348   ,
price_ratio_50016349   ,
price_ratio_50016422   ,
price_ratio_50016891   ,
price_ratio_50017300   ,
price_ratio_50018004   ,
price_ratio_50018222   ,
price_ratio_50018264   ,
price_ratio_50019095   ,
price_ratio_50019780   ,
price_ratio_50020275   ,
price_ratio_50020332   ,
price_ratio_50020485   ,
price_ratio_50020579   ,
price_ratio_50020611   ,
price_ratio_50020808   ,
price_ratio_50020857   ,
price_ratio_50022517   ,
price_ratio_50022703   ,
price_ratio_50023282   ,
price_ratio_50023575   ,
price_ratio_50023717   ,
price_ratio_50023722   ,
price_ratio_50023724   ,
price_ratio_50023804   ,
price_ratio_50023878   ,
price_ratio_50023904   ,
price_ratio_50024451   ,
price_ratio_50024612   ,
price_ratio_50024971   ,
price_ratio_50025004   ,
price_ratio_50025110   ,
price_ratio_50025111   ,
price_ratio_50025705   ,
price_ratio_50025707   ,
price_ratio_50026316   ,
price_ratio_50026523   ,
price_ratio_50026555   ,
price_ratio_50026800   ,
price_ratio_50050359   ,
price_ratio_50050471   ,
price_ratio_50074001   ,
price_ratio_50158001   ,
price_ratio_50454031   ,
price_ratio_50468001   ,
price_ratio_50510002   ,
price_ratio_99         ,
brand_id_num           ,
root_cat_id_num        ,
b_bc_price_ratio       ,
b_bc_type_num_ratio    ,
brand_effec_price_ratio ,
brand_effec_num_ratio  ,
total_price            ,
b50_ratio              ,
active_score           ,
b50_num_ratio          ,
qq_age                 ,
qq_gender              ,

case when alipay like '已通过支付宝实名认证' then 1 else 0 end  as alipay_flag  ,
buycnt  ,
cast(regexp_replace(verify, 'VIP等级', '')  as int) as  verify_level ,
(12 * (2016 - YEAR(regexp_replace(regtime, '\\.', '-'))) + (7 - MONTH(regexp_replace(regtime, '\\.', '-')))) regtime_month ,
tel_tb_num ,
tel_loc      ,
           row_number()  OVER (distribute by uid sort by buycnt) as rn
 from t_base_yhhx_model t1 join
(select uid,tel_index,count(1) as tel_tb_num  from t_zlj_phone_rank_index  group by uid ,tel_index) t2 on t1.tel_index=t2.tel_index

)t where rn=1
;


-- create table t_base_yhhx_model_tel_dup as
-- SELECT  * from
-- (
-- SELECT  t1.* ,row_number()  OVER (PARTITION BY tel ORDER BY 1 desc) as rn
--
--  from t_base_yhhx_model_tel t1
--  )t where rn=1
-- ;

-- check

162896734
SELECT  count(1) from t_base_yhhx_model_tel ;

162896734
SELECT  count(1) from (select tel  from t_base_yhhx_model_tel group by tel )t;

