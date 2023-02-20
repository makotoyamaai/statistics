##########
# q85.py #
##########
# 顧客データ(df_customer)の全顧客に対し，郵便番号(postal_cd)を用いて
# ジオコードデータ(df_geocode)を紐付け，新たな顧客データを作成せよ．
# ただし，1つの郵便番号(postal_cd)に複数の経度(longitude)，緯度(latitude)情報が紐づく場合は，
# 経度(longitude)，緯度(latitude)の平均値を算出して使用すること．
# また，作成結果を確認するために結果を10件表示せよ．

import pandas as pd

df_geocode = pd.read_csv("../data/geocode.csv", dtype={'prefecture':str, 'city':str, 'town':str, 'street':str, 'address':str, 'full_address':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})

df_geocode_1 = df_geocode.groupby('postal_cd')\
		.agg(m_longitude=('longitude', 'mean'),
		     m_latitude=('latitude', 'mean')).reset_index()

df_customer_1 = pd.merge(df_customer, df_geocode_1, how='inner', on='postal_cd')

ans85 = df_customer_1.head(10)

ans85.to_csv("../answer/ans85.csv")
print(ans85)
