##########
# q60.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)を顧客ID(customer_id)ごとに合計し，
# 売上金額合計を最小値0，最大値1に正規化して顧客ID，売上金額合計とともに10件表示せよ．
# ただし，顧客IDが"Z"から始まるものは非会員を表すため，除外して計算すること．

import pandas as pd
from sklearn import preprocessing

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt.query('not customer_id.str.startswith("Z")',
				   engine='python')\
				  .groupby('customer_id').agg({'amount':'sum'}).reset_index()

df_sales_amount['std_amount'] = preprocessing.minmax_scale(df_sales_amount['amount'])

ans60 = df_sales_amount.head(10)

ans60.to_csv("../answer/ans60.csv")
#print(ans60)
