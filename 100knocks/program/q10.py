##########
# q10.py #
##########
# 店舗データ(df_store)から，店舗コード(store_cd)が"S14"で始まるものだけ全項目抽出し，
# 10件表示せよ．

import pandas as pd

df_store = pd.read_csv("../data/store.csv", dtype={'store_cd':str, 'store_name':str, 'prefecture_cd':str, 'prefecture':str, 'address':str, 'address_kana':str})

ans10 = df_store.query('store_cd.str.startswith("S14")', engine='python').head(10)

ans10.to_csv("../answer/ans10.csv")
#print(ans10)
