#########
# q9.py #
#########
# 以下の処理において，出力結果を変えずにORをANDに書き換えよ．
# df_store.query('not(prefecture_cd == "13" | floor_area > 900)')

import pandas as pd

df_store = pd.read_csv("../data/store.csv", dtype={'store_name':str, 'prefecture_cd':str, 'prefecture':str, 'address':str, 'address_kana':str})

ans9 = df_store.query('prefecture_cd != "13" & floor_area <= 900')

ans9.to_csv("../answer/ans9.csv")
#print(ans9)
