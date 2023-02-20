##########
# q45.py #
##########
# 顧客データ(df_customer)の生年月日(birth_day)は日付型でデータを保有している．
# これをYYYYMMDD形式の文字列に変換し，顧客ID(customer_id)とともに10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})

ans45 = pd.concat([df_customer['customer_id'],
		   # translate to YYYYMMDD type string
		   pd.to_datetime(df_customer['birth_day']).dt.strftime('%Y%m%d')],
		  axis = 1).head(10)

ans45.to_csv("../answer/ans45.csv")
#print(ans45)
