##########
# q83.py #
##########
# 単価(unit_price)と原価(unit_cost)の欠損値について，
# 各商品のカテゴリ小区分コード(category_small_cd)ごとに算出した中央値で補完した
# 新たな商品データを作成せよ．
# なお，中央値については1円未満を丸めること(四捨五入または偶数への丸めで良い)．
# 補完実施後，各項目について欠損が生じていないことも確認すること．

import pandas as pd
import numpy as np

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})

df_tmp = (df_product.groupby('category_small_cd').agg(median_price=('unit_price', 'median'),
		median_cost=('unit_cost', 'median')).reset_index())

df_product_4 = pd.merge(df_product, df_tmp, how='inner', on='category_small_cd')

df_product_4['unit_price'] = df_product_4[['unit_price', 'median_price']]\
				.apply(lambda x: np.round(x[1]) if np.isnan(x[0]) else x[0], axis=1)

df_product_4['unit_cost'] = df_product_4[['unit_cost', 'median_cost']]\
				.apply(lambda x: np.round(x[1]) if np.isnan(x[0]) else x[0], axis=1)

ans83 = df_product_4.isnull().sum()

ans83.to_csv("../answer/ans83.csv")
#print(ans83)
