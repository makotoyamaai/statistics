##########
# q46.py #
##########
# 顧客データ(df_customer)の申込日(application_date)はYYYYMMDD形式の文字列型で
# データを保有している．
# これを日付型に変換し，顧客ID(customer_id)とともに10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})

ans46 = pd.concat([df_customer['customer_id'],
		   # translate to YYYY-MM-DD type string
		   pd.to_datetime(df_customer['application_date'].astype(str)).dt.strftime('%Y-%m-%d')], axis = 1).head(10)

ans46.to_csv("../answer/ans46.csv")
#print(ans46)
