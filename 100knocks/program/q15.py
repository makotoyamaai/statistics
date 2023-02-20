##########
# q15.py #
##########
# 顧客データ(df_customer)から，ステータスコード(status_cd)の先頭がアルファベットのA~Fで始まり，
# 末尾が数字の1~9で終わるデータを全項目抽出し，10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str})

ans15 = df_customer.query('status_cd.str.contains(r"^[A-F].*[1-9]$")', engine='python').head(10)

ans15.to_csv("../answer/ans15.csv")
#print(ans15)
