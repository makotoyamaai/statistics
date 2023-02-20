##########
# q43.py #
##########
# レシート明細データ(df_receipt)と顧客データ(df_customer)を結合し，
# 性別コード(gender_cd)と年代(ageから計算)ごとに売上金額(amount)を合計した
# 売上サマリデータを作成せよ．性別コードは0が男性，1が女性，9が不明を表すものとする．
# ただし，項目構成は年代，女性の売上金額，男性の売上金額，性別不明の売上金額の
# 4項目とすること(縦に年代，横に性別のクロス集計)．
# また，年代は10歳ごとの階級とすること．

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

ans43 = df_sales_summary

ans43.to_csv("../answer/ans43.csv")
#print(ans43)
