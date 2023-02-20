##########
# q84.py #
##########
# 顧客データ(df_customer)の全顧客に対して全期間の売上金額に占める2019年売上金額の割合を計算し，
# 新たなデータを作成せよ．
# ただし，売上実績がない場合は0として扱うこと．
# そして計算した割合が0超のものを抽出し，結果を10件表示せよ．
# また，作成したデータに欠損が存在しないことを確認せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_receipt_2019 = df_receipt.query('20190101 <= sales_ymd <= 20191231')\
			    .groupby('customer_id')\
			    .agg(amount_2019=('amount', 'sum'))\
			    .reset_index()

df_receipt_all = df_receipt.groupby('customer_id')\
			   .agg(amount_all=('amount', 'sum'))\
			   .reset_index()

df_sales_rate = df_customer[['customer_id']]\
		.merge(df_receipt_2019, how='left', on='customer_id')\
		.merge(df_receipt_all, how='left', on='customer_id')

df_sales_rate['amount_2019'] = df_sales_rate['amount_2019'].fillna(0)
df_sales_rate['amount_all'] = df_sales_rate['amount_all'].fillna(0)

df_sales_rate['amount_rate'] = df_sales_rate[['amount_2019', 'amount_all']]\
				.apply(lambda x: 0 if x[0] == 0 else x[0] / x[1], axis=1)

df_sales_rate['amount_rate'] = df_sales_rate['amount_rate'].fillna(0) 

ans84 = df_sales_rate.query('amount_rate > 0').head(10)

ans84.to_csv("../answer/ans84.csv")
print(ans84)
