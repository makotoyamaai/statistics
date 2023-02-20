#########
# q3.py #
#########
# レシート明細データ(df_receipt)から売上年月日(sales_ymd)，顧客ID(customer_id)，
# 商品コード(product_cd)，売上金額(amount)の順に列を指定し，10件表示せよ．
# ただし，sales_ymdをsales_dateに項目名を変更しながら抽出すること．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype=str)

ans3 = df_receipt[['sales_ymd', 'customer_id', 'product_cd', 'amount']].rename(columns={'sales_ymd':'sales_date'}).head(10)

ans3.to_csv("../answer/ans3.csv")
#print(ans3)
