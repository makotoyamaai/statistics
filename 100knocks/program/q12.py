##########
# q12.py #
##########
# 店舗データ(df_store)から，住所(address)に"横浜市"が含まれるものだけ全項目表示せよ．

import pandas as pd

df_store = pd.read_csv("../data/store.csv", dtype=str)

ans12 = df_store.query('address.str.contains("横浜市")', engine='python')

ans12.to_csv("../answer/ans12.csv")
#print(ans12)
