##########
# q23.py #
##########
# レシート明細データ(df_receipt)，店舗コード(store_cd)ごとに売上金額(amount)と
# 売上数量(quantity)を合計せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans23 = df_receipt.groupby('store_cd').agg({'amount':'sum', 'quantity':'sum'}).reset_index()

ans23.to_csv("../answer/ans23.csv")
#print(ans23)
