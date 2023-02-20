##########
# q44.py #
##########
# q43で作成した売上サマリデータ(id_sales_summary)は性別の売上を横持ちさせたものであった．
# このデータから性別を縦持ちさせ，年代，性別コード，売上金額の3項目に変換せよ．
# ただし，性別コードは男性を"00"，女性を"01"，不明を"99"とする．

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})

df_sales_amount_by_date = df_receipt[['sales_ymd', 'amount']]\

df_tmp = pd.merge(df_receipt, df_customer, how='inner', on='customer_id')

df_tmp['era'] = np.floor(df_tmp['age'] / 10).astype(int) * 10

df_sales_summary = pd.pivot_table(df_tmp, 
				  index='era', 
				  columns='gender_cd',
				  values='amount',
				  aggfunc='sum').reset_index()

df_sales_summary.columns = ['era', 'male', 'female', 'unknown']

ans44 = df_sales_summary.set_index('era')\
	.stack().reset_index().replace({'female':'01', 'male':'00', 'unknown':'99'})\
	.rename(columns={'level_1':'gender_cd', 0:'amount'})

ans44.to_csv("../answer/ans44.csv")
#print(ans44)
