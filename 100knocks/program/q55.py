##########
# q55.py #
##########
# レシート明細(df_receipt)データの売上金額(amount)を顧客ID(customer_id)ごとに合計し，
# その合計金額の四分位点を求めよ．
# その上で，顧客ごとの売上金額合計に対して以下の基準でカテゴリ値を作成し，
# 顧客ID，売上金額合計とともに10件表示せよ．
# カテゴリ値は順に1~4とする．
# ・最小値以上第1四分位未満-->1を付与
# ・第1四分位以上第2四分位未満-->2を付与
# ・第2四分位以上第3四分位未満-->3を付与
# ・第3四分位以上-->4を付与

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt[['customer_id', 'amount']]\
		.groupby('customer_id').sum().reset_index()

pct25 = np.quantile(df_sales_amount['amount'], 0.25)
pct50 = np.quantile(df_sales_amount['amount'], 0.5)
pct75 = np.quantile(df_sales_amount['amount'], 0.75)

def pct_group(x):
	if x < pct25:
		return 1
	elif pct25 <= x < pct50:
		return 2
	elif pct50 <= x < pct75:
		return 3
	elif pct75 <= x:
		return 4

df_sales_amount['pct_group'] = df_sales_amount['amount'].apply(pct_group)

ans55 = df_sales_amount.head(10)

ans55.to_csv("../answer/ans55.csv")
#print(ans55)
#print('pct25: ', pct25)
#print('pct50: ', pct50)
#print('pct75: ', pct75)
