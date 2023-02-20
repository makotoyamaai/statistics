##########
# q26.py #
##########
# レシート明細データ(df_receipt)に対し，顧客ID(customer_id)ごとに
# 最も新しい売上年月日(sales_ymd)と古い売上年月日を求め，
# 両者が異なるデータを10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

df_tmp = df_receipt.groupby('customer_id').agg({'sales_ymd':['max','min']}).reset_index()
df_tmp.columns = ['customer_id', 'sales_ymd_max', 'sales_ymd_min']
ans26 = df_tmp.query('sales_ymd_max != sales_ymd_min').head(10)

ans26.to_csv("../answer/ans26.csv")
#print(ans26)
