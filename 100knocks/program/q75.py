##########
# q75.py #
##########
# 顧客データ(df_customer)からランダムに1%のデータを抽出し，先頭から10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

ans75 = df_customer.sample(frac=0.01).head(10)

ans75.to_csv("../answer/ans75.csv")
#print(ans75)
