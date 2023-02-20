##########
# q70.py #
##########
# レシート明細データ(df_receipt)の売上日(sales_ymd)に対し，
# 顧客データ(df_customer)の会員申込日(application_date)からの経過日数を計算し，
# 顧客ID(customer_id)，売上日，会員申込日とともに10件表示せよ．
# sales_ymdは数値，application_dateは文字列でデータを保持している点に注意．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_tmp = df_receipt[['customer_id', 'sales_ymd']].drop_duplicates()

df_tmp = pd.merge(df_tmp, df_customer[['customer_id', 'application_date']],
					how='inner', on='customer_id')

df_tmp['sales_ymd'] = pd.to_datetime(df_tmp['sales_ymd'].astype(str))
df_tmp['application_date'] = pd.to_datetime(df_tmp['application_date'].astype(str))
df_tmp['elapsed_days'] = df_tmp['sales_ymd'] - df_tmp['application_date']
df_tmp['elapsed_days'] = df_tmp['elapsed_days'].dt.days

ans70 = df_tmp.head(10)

ans70.to_csv("../answer/ans70.csv")
#print(ans70)
