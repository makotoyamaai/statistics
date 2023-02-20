##########
# q78.py #
##########
# レシート明細データ(df_receipt)の売上金額を顧客単位に合計し，合計した売上金額の外れ値を抽出せよ．
# ただし，顧客IDが"Z"から始まるものは非会員を表すため，除外して計算すること．
# なお，ここでは外れ値を第1四分位と第3四分位の差であるIQRを用いて，
# 「第1四分位数-1.5xIQR」を下回るもの，または「第3四分位数+1.5xIQR」を超えるものとする．
# 結果は10件表示せよ．

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt.query('not customer_id.str.startswith("Z")',
				   engine='python')\
				  .groupby('customer_id')\
				  .agg({'amount':'sum'}).reset_index()

pct25 = np.percentile(df_sales_amount['amount'], q=25)
pct75 = np.percentile(df_sales_amount['amount'], q=75)

iqr = pct75 - pct25
amount_low = pct25 - (iqr * 1.5)
amount_high = pct75 + (iqr * 1.5)

ans78 = df_sales_amount.query('amount < @amount_low or @amount_high < amount').head(10)

ans78.to_csv("../answer/ans78.csv")
#print(ans78)
