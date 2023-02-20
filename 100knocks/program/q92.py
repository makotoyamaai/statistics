##########
# q92.py #
##########
# 顧客データ(df_customer)の性別について，第三正規形へと正規化せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_gender_std = df_customer[['gender_cd', 'gender']].drop_duplicates()

df_customer_std = df_customer.drop(columns='gender')

ans92_1 = df_customer_std.head(3)
ans92_2 = df_gender_std.head(3)

ans92_1.to_csv("../answer/ans92_1.csv")
ans92_2.to_csv("../answer/ans92_2.csv")
#print(ans92_1)
#print(ans92_2)
