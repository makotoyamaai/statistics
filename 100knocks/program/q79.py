##########
# q79.py #
##########
# 商品データ(df_product)の各項目に対し，欠損値を確認せよ．

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})

ans79 = df_product.isnull().sum()

ans79.to_csv("../answer/ans79.csv")
#print(ans79)
