##########
# q29.py #
##########
# レシート明細データ(df_receipt)に対し，店舗コード(store_cd)ごとに
# 商品コード(product_cd)の最頻値を求め，10件表示させよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans29 = df_receipt.groupby('store_cd').product_cd.apply(lambda x: x.mode()).reset_index().head(10)

ans29.to_csv("../answer/ans29.csv")
#print(ans29)
