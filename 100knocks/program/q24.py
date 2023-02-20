##########
# q24.py #
##########
# レシート明細データ(df_receipt)に対し，顧客ID(customer_id)ごとに
# 最も新しい売上年月日(sales_ymd)を求め，10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans24 = df_receipt.groupby('customer_id').agg({'sales_ymd':'max'}).reset_index().head(10)

ans24.to_csv("../answer/ans24.csv")
#print(ans24)
