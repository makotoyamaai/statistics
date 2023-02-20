##########
# q37.py #
##########
# 商品データ(df_product)とカテゴリデータ(df_category)を内部結合し，
# 商品データの全項目とカテゴリデータのカテゴリ小区分名(category_small_name)を
# 10件表示せよ．

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str})
df_category = pd.read_csv("../data/category.csv", dtype={'category_major_name':str, 'category_medium_name':str, 'category_small_name':str})

ans37 = pd.merge(df_product, df_category[['category_small_cd', 'category_small_name']], how='inner', on='category_small_cd').head(10)

ans37.to_csv("../answer/ans37.csv")
#print(ans37)
