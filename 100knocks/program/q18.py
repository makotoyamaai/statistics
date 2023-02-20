##########
# q18.py #
##########
# 顧客データ(df_customer)を生年月日(birth_day)で若い順にソートし，先頭から全項目を10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'store_cd':str, 'status_cd':str})

ans18 = df_customer.sort_values('birth_day', ascending=False).head(10)

ans18.to_csv("../answer/ans18.csv")
#print(ans18)
