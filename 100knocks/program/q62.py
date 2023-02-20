##########
# q62.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)を顧客ID(customer_id)ごとに合計し，
# 売上金額合計を自然対数化(底e)して顧客ID，売上金額合計とともに10件表示せよ．
# ただし，顧客IDが"Z"から始まるものは非会員を表すため，除外して計算すること．

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt.query('not customer_id.str.startswith("Z")',
				   engine='python')\
				  .groupby('customer_id').agg({'amount':'sum'}).reset_index()

df_sales_amount['log_amount'] = np.log(df_sales_amount['amount'] + 0.5)

ans62 = df_sales_amount.head(10)

ans62.to_csv("../answer/ans62.csv")
#print(ans62)
