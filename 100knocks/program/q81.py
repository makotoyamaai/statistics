##########
# q81.py #
##########
# 単価(unit_price)と原価(unit_cost)の欠損値について，それぞれの平均値で補完した
# 新たな商品データを作成せよ．
# なお，平均値については1円未満を丸めること(四捨五入または偶数への丸めで良い)．
# 補完実施後，各項目について欠損が生じていないことも確認すること．

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})

imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_values = imp_mean.fit_transform(df_product[['unit_price', 'unit_cost']])

df_product_2 = df_product.copy()
df_product_2[['unit_price', 'unit_cost']] = imp_values.round()

ans81 = df_product_2.isnull().sum()

ans81.to_csv("../answer/ans81.csv")
#print(ans81)
