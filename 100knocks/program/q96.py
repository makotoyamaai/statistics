##########
# q96.py #
##########
# q93で作成したカテゴリ名付き商品データを以下の仕様でファイル出力せよ．
# |ファイル形式|ヘッダ有無|文字エンコーディング||:--:|:--:|:--:||CSV(カンマ区切り)|無し|UTF-8|
# ファイル出力先のパスは以下のようにすること
# |出力先||:--:||./data|

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})
df_category = pd.read_csv("../data/category.csv", dtype={'category_major_name':str, 'category_medium_name':str, 'category_small_name':str})

df_product_full = pd.merge(df_product, df_category[['category_small_cd',
						    'category_major_name',
						    'category_medium_name',
						    'category_small_name']],
			   how='inner', on='category_small_cd')

ans96 = df_product_full

ans96.to_csv("../answer/ans96.csv", header=False, encoding='UTF-8', index=False)
#print(ans96)
