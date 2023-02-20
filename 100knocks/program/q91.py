##########
# q91.py #
##########
# 顧客データ(df_customer)の各顧客に対し，売上実績がある顧客数と売上実績がない顧客数が
# 1:1となるようにアンダーサンプリングで抽出せよ．

import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_tmp = df_receipt.groupby('customer_id').agg({'amount':'sum'}).reset_index()

df_tmp = pd.merge(df_customer, df_tmp, how='left', on='customer_id')

df_tmp['is_buy_flag'] = np.where(df_tmp['amount'].isnull(), 0, 1)

rs = RandomUnderSampler(random_state=71)

df_down_sampling, _ = rs.fit_resample(df_tmp, df_tmp.is_buy_flag)

ans91_1 = len(df_down_sampling.query('is_buy_flag == 0'))
ans91_2 = len(df_down_sampling.query('is_buy_flag == 1'))

data = {'0の件数':[ans91_1],
	'1の件数':[ans91_2]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans91.csv")
print('0の件数: ', ans91_1,
      '1の件数: ', ans91_2)
