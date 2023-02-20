##########
# q72.py #
##########
# レシート明細データ(df_receipt)の売上日(sales_ymd)に対し，
# 顧客データ(df_customer)の会員申込日(application_date)からの経過年数を計算し，
# 顧客ID(customer_id)，売上日，会員申込日とともに10件表示せよ．
# sales_ymdは数値，application_dateは文字列でデータを保持している点に注意．
# 1年未満は切り捨てること．

import pandas as pd
from dateutil.relativedelta import relativedelta

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_tmp = df_receipt[['customer_id', 'sales_ymd']].drop_duplicates()

df_tmp = pd.merge(df_tmp, df_customer[['customer_id', 'application_date']],
					how='inner', on='customer_id')

df_tmp['sales_ymd'] = pd.to_datetime(df_tmp['sales_ymd'].astype(str))
df_tmp['application_date'] = pd.to_datetime(df_tmp['application_date'].astype(str))
df_tmp['elapsed_years'] = df_tmp[['sales_ymd', 'application_date']]\
				.apply(lambda x: relativedelta(x[0], x[1]).years, axis=1)

ans72 = df_tmp.head(10)

ans72.to_csv("../answer/ans72.csv")
#print(ans72)
