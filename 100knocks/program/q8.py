#########
# q8.py #
#########
# レシート明細データ(df_receipt)から売上年月日(sales_ymd)，顧客ID(customer_id)，
# 商品コード(product_cd)，売上金額(amount)の順に列を指定し，
# 以下の条件を満たすデータを抽出せよ．
# ・顧客ID(customer_id)が"CS018205000001"
# ・商品コード(product_cd)が"P071401019"以外

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'customer_id':str, 'product_cd':str})

ans8 = df_receipt[['sales_ymd', 'customer_id', 'product_cd', 'amount']].query('customer_id == "CS018205000001" & product_cd != "P071401019"')

ans8.to_csv("../answer/ans8.csv")
#print(ans8)
