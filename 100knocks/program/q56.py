##########
# q56.py #
##########
# 顧客データ(df_customer)の年齢(age)をもとに10歳刻みで年代を算出し，顧客ID(customer_id)，
# 生年月日(birth_day)とともに10件表示せよ．
# ただし，60歳以上はすべて60歳代とすること．年代を表すカテゴリ名は任意とする．

import pandas as pd
import numpy as np

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})

df_customer_era = df_customer[['customer_id', 'birth_day']].copy()

df_customer_era['era'] = pd.cut(df_customer['age'],
				bins=[0, 10, 20, 30, 40, 50, 60, np.inf],
				right=False)

ans56 = df_customer_era[['customer_id', 'birth_day', 'era']].head(10)

ans56.to_csv("../answer/ans56.csv")
#print(ans56)
