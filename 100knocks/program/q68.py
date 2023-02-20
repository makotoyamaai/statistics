##########
# q68.py #
##########
# 商品データ(df_product)の各商品について，消費税率10%の税込金額を求めよ．
# 1円未満の端数は切り捨てとし，結果を10件表示せよ．
# ただし，単価(unit_price)には欠損が生じていることに注意せよ．

import pandas as pd
import numpy as np

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str})

df_tmp = df_product[['product_cd', 'unit_price']].copy()

df_tmp['tax_price'] = np.floor(df_tmp['unit_price'] * 1.1)

ans68 = df_tmp.head(10)

ans68.to_csv("../answer/ans68.csv")
#print(ans68)
