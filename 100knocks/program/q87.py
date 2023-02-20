##########
# q87.py #
##########
# 顧客データ(df_customer)では，異なる店舗での申込みなどにより同一顧客が複数登録されている．
# 名前(customer_name)と郵便番号(postal_cd)が同じ顧客は同一顧客と見なして1顧客1レコードとなるように
# 名寄せした名寄顧客データを作成し，顧客データの件数，名寄顧客データの件数，重複数を算出せよ．
# ただし，同一顧客に対しては売上金額合計が最も高いものを残し，
# 売上金額合計が同一もしくは売上実績がない顧客については顧客ID(customer_id)の番号が小さいものを
# 残すこととする．

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
			      
ans87_1 = len(df_customer)
ans87_2 = len(df_customer_u)
ans87_3 = len(df_customer) - len(df_customer_u)

data = {'df_customer_cnt':[ans87_1],
	'df_customer_u_cnt':[ans87_2],
	'diff':[ans87_3]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans87.csv")
print('df_customer_cnt: ', ans87_1,
      'df_customer_u_cnt: ', ans87_2,
      'diff: ', ans87_3)
