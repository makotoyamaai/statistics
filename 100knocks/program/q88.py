##########
# q88.py #
##########
# q87で作成したデータを元に，顧客データに統合名寄IDを付与したデータを作成せよ．
# ただし，統合名寄IDは以下の仕様で付与するものとする．
# ・重複していない顧客: 顧客ID(customer_id)を設定
# ・重複している顧客: 前設問で抽出したレコードの顧客IDを設定
# 顧客IDのユニーク件数と，統合名寄IDのユニーク件数の差も確認すること．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_receipt_tmp = df_receipt.groupby('customer_id')\
		.agg(sum_amount=('amount', 'sum')).reset_index()

df_customer_u = pd.merge(df_customer, df_receipt_tmp, how='left', on='customer_id')

df_customer_u['sum_amount'] = df_customer_u['sum_amount'].fillna(0)

df_customer_u = df_customer_u.sort_values(['sum_amount', 'customer_id'],
					  ascending=[False, True])

df_customer_u.drop_duplicates(subset=['customer_name', 'postal_cd'],
			      keep='first', inplace=True)
			      
df_customer_n = pd.merge(df_customer,
			 df_customer_u[['customer_name', 'postal_cd', 'customer_id']],
			 how='inner', on=['customer_name', 'postal_cd'])

df_customer_n.rename(columns={'customer_id_x':'customer_id',
			      'customer_id_y':'integration_id'}, inplace=True)


ans88 = len(df_customer_n['customer_id'].unique()) - len(df_customer_n['integration_id'].unique())

data = {'ID数の差':[ans88]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans88.csv")
print('ID数の差: ', ans88)
