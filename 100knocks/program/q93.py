##########
# q93.py #
##########
# 商品データ(df_product)では各カテゴリのコード値だけを保有し，カテゴリ名は保有していない．
# カテゴリデータ(df_category)と組み合わせて非正規化し，カテゴリ名を保有した新たな商品データを作成せよ．

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})
df_category = pd.read_csv("../data/category.csv", dtype={'category_major_name':str, 'category_medium_name':str, 'category_small_name':str})

df_product_full = pd.merge(df_product, df_category[['category_small_cd',
						    'category_major_name',
						    'category_medium_name',
						    'category_small_name']],
			   how='inner', on='category_small_cd')

ans93 = df_product_full

ans93.to_csv("../answer/ans93.csv")
#print(ans93.head(3))
