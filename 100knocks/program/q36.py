##########
# q36.py #
##########
# レシート明細データ(df_receipt)と店舗データ(df_store)を内部結合し，
# レシート明細データの全項目と店舗データの店舗名(store_name)を10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})
df_store = pd.read_csv("../data/store.csv", dtype={'store_cd':str, 'store_name':str})

ans36 = pd.merge(df_receipt, df_store[['store_cd', 'store_name']], how='inner', on='store_cd').head(10)

ans36.to_csv("../answer/ans36.csv")
#print(ans36)
