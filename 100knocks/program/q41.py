##########
# q41.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)を日付(sales_ymd)ごとに集計し，
# 前回売上があった日からの売上金額増減を計算せよ．
# そして結果を10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount_by_date = df_receipt[['sales_ymd', 'amount']]\
	.groupby('sales_ymd').sum().reset_index()

df_sales_amount_by_date = pd.concat([df_sales_amount_by_date,
				     df_sales_amount_by_date.shift()], axis=1)

df_sales_amount_by_date.columns = ['sales_ymd', 'amount', 'lag_ymd', 'lag_amount']

df_sales_amount_by_date['diff_amount'] =\
	df_sales_amount_by_date['amount'] - df_sales_amount_by_date['lag_amount']

ans41 = df_sales_amount_by_date.head(10)

ans41.to_csv("../answer/ans41.csv")
#print(ans41)
