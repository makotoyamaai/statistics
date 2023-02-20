##########
# q63.py #
##########
# 商品データ(df_product)の単価(unit_price)と原価(unit_cost)から各商品の利益額を算出し，
# 結果を10件表示せよ．

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str})

df_tmp = df_product.copy()

df_tmp['unit_profit'] = df_tmp['unit_price'] - df_tmp['unit_cost']

ans63 = df_tmp.head(10)

ans63.to_csv("../answer/ans63.csv")
#print(ans63)
