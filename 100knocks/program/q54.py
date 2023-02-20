##########
# q54.py #
##########
# 顧客データ(df_customer)の住所(address)は，埼玉県，千葉県，東京都，神奈川県のいずれかとなっている．
# 都道府県ごとにコード値を作成し，顧客ID，住所とともに10件表示せよ．
# 値は埼玉県を11，千葉県を12，東京都を13，神奈川県を14とすること．

import pandas as pd

df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'address':str, 'application_store_cd':str})

df_customer_tmp = df_customer[['customer_id', 'address']].copy()

df_customer_tmp['prefecture_cd'] = \
	df_customer['address'].str[0:3].map({'埼玉県':'11',
					     '千葉県':'12',
					     '東京都':'13',
					     '神奈川':'14'})

ans54 = df_customer_tmp.head(10)

ans54.to_csv("../answer/ans54.csv")
#print(ans54)
