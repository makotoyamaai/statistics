##########
# q58.py #
##########
# 顧客データ(df_customer)の性別コード(gender_cd)をダミー変数化し，
# 顧客ID(customer_id)とともに10件表示せよ．

import pandas as pd
import numpy as np

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

ans58 = pd.get_dummies(df_customer[['customer_id', 'gender_cd']], columns=['gender_cd']).head(10)

ans58.to_csv("../answer/ans58.csv")
#print(ans58)
