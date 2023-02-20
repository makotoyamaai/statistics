##########
# q73.py #
##########
# レシート明細データ(df_receipt)の売上日(sales_ymd)に対し，
# 顧客データ(df_customer)の会員申込日(application_date)からのエポック秒による経過時間を計算し，
# 顧客ID(customer_id)，売上日，会員申込日とともに10件表示せよ．
# sales_ymdは数値，application_dateは文字列でデータを保持している点に注意．
# なお，時間情報は保有していないため各日付は0時0分0秒を表すものとする．

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_tmp = df_receipt[['customer_id', 'sales_ymd']].drop_duplicates()

df_tmp = pd.merge(df_tmp, df_customer[['customer_id', 'application_date']],
					how='inner', on='customer_id')

df_tmp['sales_ymd'] = pd.to_datetime(df_tmp['sales_ymd'].astype(str))
df_tmp['application_date'] = pd.to_datetime(df_tmp['application_date'].astype(str))
df_tmp['elapsed_epoch'] = df_tmp['sales_ymd'].view(np.int64) -  df_tmp['application_date'].view(np.int64)
df_tmp['elapsed_epoch'] = df_tmp['elapsed_epoch'] / 10**9

ans73 = df_tmp.head(10)

ans73.to_csv("../answer/ans73.csv")
#print(ans73)
