##########
# q65.py #
##########
# 商品データ(df_product)の各商品について，利益率が30%となる新たな単価を求めよ．
# ただし，1円未満は切り捨てること．
# そして結果を10件表示させ，利益率がおよそ30%付近であることを確認せよ．
# ただし，単価(unit_price)と原価(unit_cost)には欠損が生じていることに注意せよ．

import pandas as pd
import numpy as np

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str})

df_tmp = df_product[['product_cd', 'unit_price', 'unit_cost']].copy()

df_tmp['new_price'] = np.floor(df_tmp['unit_cost'] / 0.7)

df_tmp['new_profit_rate'] = (df_tmp['new_price'] - df_tmp['unit_cost']) / df_tmp['new_price']

ans65 = df_tmp.head(10)

ans65.to_csv("../answer/ans65.csv")
#print(ans65)
