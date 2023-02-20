##########
# q40.py #
##########
# すべての店舗とすべての商品を組み合わせたデータを作成したい．
# 店舗データ(df_store)と商品データ(df_product)を直積し，件数を計算せよ．

import pandas as pd

df_store = pd.read_csv("../data/store.csv", dtype={'store_cd':str, 'store_name':str})
df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str})

df_store_tmp = df_store.copy()
df_product_tmp = df_product.copy()

df_store_tmp['key'] = 0
df_product_tmp['key'] = 0

ans40 = len(pd.merge(df_store_tmp, df_product_tmp, how='outer', on='key'))

data = {'direct product':[ans40]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans40.csv")
#print(ans40)
