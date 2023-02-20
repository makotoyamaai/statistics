##########
# q59.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)を顧客ID(customer_id)ごとに合計し，
# 売上金額合計を平均0，標準偏差1に標準化して顧客ID，売上金額合計とともに10件表示せよ．
# 標準化に使用する標準偏差は，分散の平方根，もしくは不偏分散の平方根のどちらでも良いものとする．
# ただし，顧客IDが"Z"から始まるものは非会員を表すため，除外して計算すること．

import pandas as pd
from sklearn import preprocessing

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt.query('not customer_id.str.startswith("Z")',
				   engine='python')\
				  .groupby('customer_id').agg({'amount':'sum'}).reset_index()

df_sales_amount['std_amount'] = preprocessing.scale(df_sales_amount['amount'])

ans59 = df_sales_amount.head(10)

ans59.to_csv("../answer/ans59.csv")
#print(ans59)
