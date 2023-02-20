##########
# q28.py #
##########
# レシート明細データ(df_receipt)に対し，店舗コード(store_cd)ごとに
# 売上金額(amount)の中央値を計算し，降順でTOP5を表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans28 = df_receipt.groupby('store_cd').agg({'amount':'median'}).reset_index().sort_values('amount', ascending=False).head(5)

ans28.to_csv("../answer/ans28.csv")
#print(ans28)
