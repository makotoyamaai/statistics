##########
# q69.py #
##########
# レシート明細データ(df_receipt)と商品データ(df_product)を結合し，
# 顧客ごとに全商品の売上金額合計と，カテゴリ大区分コード(category_major_cd)が
# "07"(瓶詰缶詰)の売上金額合計を計算の上，両者の比率を求めよ．
# 抽出対象はカテゴリ大区分コード"07"(瓶詰缶詰)の売上実績がある顧客のみとし，
# 結果を10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_product = pd.read_csv("../data/product.csv", dtype={'product_cd':str, 'category_major_cd':str})

df_tmp_1 = df_receipt.groupby('customer_id').agg({'amount':'sum'})\
		.reset_index().rename(columns={'amount':'sum_all'})
		
df_tmp_2 = pd.merge(df_receipt, df_product.query('category_major_cd == "07"'),
		how='inner', on='product_cd').groupby('customer_id')\
		.agg({'amount':'sum'}).reset_index()\
		.rename(columns={'amount':'sum_07'})
				
df_tmp_3 = pd.merge(df_tmp_1, df_tmp_2, how='inner', on='customer_id')

df_tmp_3['sales_rate'] = df_tmp_3['sum_07'] / df_tmp_3['sum_all']

ans69 = df_tmp_3.head(10)

ans69.to_csv("../answer/ans69.csv")
#print(ans69)
