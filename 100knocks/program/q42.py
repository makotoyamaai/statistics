##########
# q42.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)を日付(sales_ymd)ごとに集計し，
# 各日付のデータに対し，前回，前々回，3回前に売上があった日のデータを結合せよ．
# そして結果を10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount_by_date = df_receipt[['sales_ymd', 'amount']]\
	.groupby('sales_ymd').sum().reset_index()

for i in range(1, 4):
	df_tmp = pd.concat([df_sales_amount_by_date,
			    df_sales_amount_by_date.shift(i)], axis=1)
	
	if i==1:
		df_lag = df_tmp
	else:
		df_lag = df_lag.append(df_tmp)

df_lag.columns = ['sales_ymd', 'amount', 'lag_ymd', 'lag_amount']

ans42 = df_lag.dropna().astype(int).sort_values(['sales_ymd', 'lag_ymd']).head(10)

ans42.to_csv("../answer/ans42.csv")
#print(ans42)
