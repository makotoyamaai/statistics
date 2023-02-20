##########
# q52.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)を顧客ID(customer_id)ごとに合計の上，
# 売上金額合計に対して2,000円以下を0，2,000円より大きい金額を1に二値化し，
# 顧客ID，売上金額合計とともに10件表示せよ．
# ただし，顧客IDが"Z"から始まるものは非会員を表すため，除外して計算すること．

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt.query('not customer_id.str.startswith("Z")', engine='python')

df_sales_amount = df_sales_amount[['customer_id', 'amount']]\
				   .groupby('customer_id').sum().reset_index()

df_sales_amount['sales_fig'] = np.where(df_sales_amount['amount'] > 2000, 1, 0)

ans52 = df_sales_amount.head(10)

ans52.to_csv("../answer/ans52.csv")
#print(ans52)
