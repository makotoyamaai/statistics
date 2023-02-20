##########
# q53.py #
##########
# 顧客データ(df_customer)の郵便番号(postal_cd)に対し，東京(先頭3桁が100~209のもの)を1，
# それ以外のものを0に二値化せよ．
# さらにレシート明細データ(df_receipt)と結合し，全期間において売上実績のある顧客数を，
# 作成した日ごとにカウントせよ．

import pandas as pd
import numpy as np

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})
df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_tmp = df_customer[['customer_id', 'postal_cd']].copy()

df_tmp['postal_fig'] = np.where(df_tmp['postal_cd'].str[0:3].astype(int)\
				.between(100, 209), 1, 0)

ans53 = pd.merge(df_tmp, df_receipt, how='inner', on='customer_id')\
		 .groupby('postal_fig').agg({'customer_id':'nunique'})

ans53.to_csv("../answer/ans53.csv")
#print(ans53)
