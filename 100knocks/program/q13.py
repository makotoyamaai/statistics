##########
# q13.py #
##########
# 顧客データ(df_customer)から，ステータスコード(status_cd)の先頭がアルファベットのA~Fで始まる
# データを全項目抽出し，10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype=str)

ans13 = df_customer.query('status_cd.str.contains(r"^[A-F]")', engine='python').head(10)

ans13.to_csv("../answer/ans13.csv")
#print(ans13)
