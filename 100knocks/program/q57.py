##########
# q57.py #
##########
# q56の抽出結果と性別コード(gender_cd)により，新たに性別x年代の組み合わせを表す
# カテゴリデータを作成し，10件表示せよ．
# 組み合わせを表すカテゴリの値は任意とする．

import pandas as pd
import numpy as np

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_customer_era = df_customer[['customer_id', 'birth_day']].copy()

df_customer_era['era'] = pd.cut(df_customer['age'],
				bins=[0, 10, 20, 30, 40, 50, 60, np.inf],
				right=False)

df_customer_era['gender_era'] =\
	df_customer['gender_cd'] + df_customer_era['era'].astype(str).str.zfill(2)

ans57 = df_customer_era.head(10)

ans57.to_csv("../answer/ans57.csv")
#print(ans57)
