##########
# q33.py #
##########
# レシート明細データ(df_receipt)に対し，店舗コード(store_cd)ごとに
# 売上金額(amount)の平均を計算し，330以上のものを抽出せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans33 = df_receipt.groupby('store_cd').agg({'amount':'mean'}).reset_index().query('amount >= 330')

ans33.to_csv("../answer/ans33.csv")
#print(ans33)
