##########
# q39.py #
##########
# レシート明細データ(df_receipt)から，売上日数の多い顧客の上位20件を抽出したデータと，
# 売上金額合計の多い顧客の上位20件を抽出したデータをそれぞれ作成し，
# さらにその2つを完全外部結合せよ．
# ただし，非会員(顧客IDが"Z"から始まるもの)は除外すること．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_data = df_receipt.query('not customer_id.str.startswith("Z")', engine='python')

df_day = df_data[~df_data.duplicated(subset=['customer_id', 'sales_ymd'])]\
	.groupby('customer_id').sales_ymd.count().reset_index()\
	.sort_values('sales_ymd', ascending=False).head(20)

df_sum = df_data.groupby('customer_id').amount.sum().reset_index()\
	.sort_values('amount', ascending=False).head(20)

ans39 = pd.merge(df_day, df_sum, how='outer', on='customer_id')

ans39.to_csv("../answer/ans39.csv")
#print(ans39)
