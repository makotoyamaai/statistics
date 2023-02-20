##########
# q89.py #
##########
# 売上実績がある顧客を，予測モデル構築のため学習用データとテスト用データに分割したい．
# それぞれ8:2の割合でランダムにデータを分割せよ．

import pandas as pd
from sklearn.model_selection import train_test_split

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_sales_customer = df_receipt.groupby('customer_id').agg({'amount':sum}).reset_index()

df_sales_customer = df_sales_customer.query('amount > 0')

df_tmp = pd.merge(df_customer, df_sales_customer['customer_id'], how='inner', on='customer_id')

df_train, df_test = train_test_split(df_tmp, test_size=0.2, random_state=71)

ans89_1 = len(df_train) / len(df_tmp)
ans89_2 = len(df_test) / len(df_tmp)

data = {'学習データ割合':[ans89_1],
	'テストデータ割合':[ans89_2]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans89.csv")
print('学習データ割合: ', ans89_1,
      'テストデータ割合: ', ans89_2)
