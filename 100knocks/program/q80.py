##########
# q80.py #
##########
# 商品データ(df_product)のいずれかの項目に欠損が発生しているレコードをすべて削除した
# 新たな商品データを作成せよ．
# なお，削除前後の件数を表示させ，q79で確認した件数だけ減少していることも確認すること．

import pandas as pd

df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})

df_product_1 = df_product.copy()

df_product_1.dropna(inplace=True)

ans80_1 = len(df_product)
ans80_2 = len(df_product_1)

data = {'削除前':[ans80_1],
	'削除後':[ans80_2]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans80.csv")

print('削除前: ', ans80_1)
print('削除後: ', ans80_2)
