##########
# q38.py #
##########
# 顧客データ(df_customer)とレシート明細データ(df_receipt)から，
# 顧客ごとの売上金額合計を求め，10件表示せよ．
# ただし，売上実績がない顧客については売上金額を0として表示させること．
# また，顧客は性別コード(gender_cd)が女性(1)であるものを対象とし，
# 非会員(顧客IDが"Z"から始まるもの)は除外すること．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})
df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_amount_sum = df_receipt.groupby('customer_id').amount.sum().reset_index()

df_tmp = df_customer.query('gender_cd == "1"' and 'not customer_id.str.startswith("Z")', engine='python')

ans38 = pd.merge(df_tmp['customer_id'], df_amount_sum, how='left', on='customer_id').fillna(0).head(10)

ans38.to_csv("../answer/ans38.csv")
#print(ans38)
