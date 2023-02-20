##########
# q64.py #
##########
# 商品データ(df_product)の単価(unit_price)と原価(unit_cost)から，
# 各商品の利益率の全体平均を算出せよ．
# ただし，単価と原価には欠損が生じていることに注意せよ．

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str})

df_tmp = df_product.copy()

df_tmp['unit_profit_rate'] = (df_tmp['unit_price'] - df_tmp['unit_cost']) / df_tmp['unit_price']

ans64 = df_tmp['unit_profit_rate'].mean(skipna=True)

data = {'mean':[ans64]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans64.csv")
#print(ans64)
