##########
# q14.py #
##########
# 顧客データ(df_customer)から，ステータスコード(status_cd)の末尾が数字の1~9で終わる
# データを全項目抽出し，10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str})

ans14 = df_customer.query('status_cd.str.contains(r"[1-9]$", regex=True)', engine='python').head(10)

ans14.to_csv("../answer/ans14.csv")
#print(ans14)
