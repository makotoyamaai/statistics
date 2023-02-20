##########
# q16.py #
##########
# 店舗データ(df_store)から，電話番号(tel_no)が3桁-3桁-4桁のデータを全項目表示せよ．

import pandas as pd

df_store = pd.read_csv("../data/store.csv", dtype=str)

ans16 = df_store.query('tel_no.str.contains(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$")', engine='python')

ans16.to_csv("../answer/ans16.csv")
#print(ans16)
