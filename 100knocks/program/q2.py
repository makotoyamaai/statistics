#########
# q2.py #
#########
# レシート明細データ(df_receipt)から売上年月日(sales_ymd)，顧客ID(customer_id)，
# 商品コード(product_cd)，売上金額(amount)の順に列を指定し，10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype=str)

ans2 = df_receipt[['sales_ymd', 'customer_id', 'product_cd', 'amount']].head(10)

ans2.to_csv("../answer/ans2.csv")
#print(ans2)
