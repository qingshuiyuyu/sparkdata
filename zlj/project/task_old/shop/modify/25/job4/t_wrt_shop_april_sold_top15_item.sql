CREATE TABLE  t_wrt_shop_april_sold_top15_item as

SELECT
  shop_id,
  item_id,
  title,
  sold,
  sales,
  rn
FROM
  (
    SELECT
      shop_id,
      item_id,
      title,
      sold,
      sales,
      ROW_NUMBER()
      OVER (PARTITION BY shop_id
        ORDER BY sold DESC) AS rn
    FROM
      (
        SELECT
          item_id,
          shop_id,
          max(title)             AS title,
          cast(sum(sold) AS INT) AS sold,
          sum(sales)             AS sales
        FROM
          t_wrt_tmp_14shop_totalsold
        WHERE ds < 20160500
        GROUP BY item_id, shop_id
      ) t
  ) tt
WHERE rn < 16;