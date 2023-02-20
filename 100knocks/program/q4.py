#########
# q4.py #
#########
# レシート明細データ(df_receipt)から売上年月日(sales_ymd)，顧客ID(customer_id)，
# 商品コード(product_cd)，売上金額(amount)の順に列を指定し，
# 以下の条件を満たすデータを抽出せよ．
# ・顧客ID(customer_id)が"CS018205000001"

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype=str)

ans4 = df_receipt[['sales_ymd', 'customer_id', 'product_cd', 'amount']].query('customer_id == "CS018205000001"')

ans4.to_csv("../answer/ans4.csv")
#print(ans4)
