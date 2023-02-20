##########
# q76.py #
##########
# 顧客データ(df_customer)から性別コード(gender_cd)の割合に基づき
# ランダムに10%のデータを層化抽出し，性別コードごとに件数を集計せよ．

import pandas as pd
from sklearn.model_selection import train_test_split

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

_, df_tmp = train_test_split(df_customer, test_size=0.1, stratify=df_customer['gender_cd'])

ans76 = df_tmp.groupby('gender_cd').agg({'customer_id':'count'}) 

ans76.to_csv("../answer/ans76.csv")
#print(ans76)
