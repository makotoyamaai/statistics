##########
# q11.py #
##########
# 顧客データ(df_customer)から顧客ID(customer_id)の末尾が1のものだけ全項目抽出し，
# 10件表示せよ．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype=str)

ans11 = df_customer.query('customer_id.str.endswith("1")', engine='python').head(10)

ans11.to_csv("../answer/ans11.csv")
#print(ans11)
