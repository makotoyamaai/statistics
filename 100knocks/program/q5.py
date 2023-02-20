#########
# q5.py #
#########
# レシート明細データ(df_receipt)から売上年月日(sales_ymd)，顧客ID(customer_id)，
# 商品コード(product_cd)，売上金額(amount)の順に列を指定し，
# 以下の条件を満たすデータを抽出せよ．
# ・顧客ID(customer_id)が"CS018205000001"
# ・売上金額(amount)が1,000以上

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'customer_id':str, 'product_cd':str})

ans5 = df_receipt[['sales_ymd', 'customer_id', 'product_cd', 'amount']].query('customer_id == "CS018205000001" & amount >= 1000')

ans5.to_csv("../answer/ans5.csv")
#print(ans5)
