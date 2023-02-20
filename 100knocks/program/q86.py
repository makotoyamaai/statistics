##########
# q86.py #
##########
# q85で作成した緯度経度付き顧客データに対し，会員申込店舗コード(application_store_cd)を
# キーに店舗データ(df_store)と結合せよ．
# そして申込み店舗の緯度(latitude)・経度情報(longitude)と顧客住所(address)の緯度・経度を用いて
# 申込み店舗と顧客住所の距離(単位:km)を求め，顧客ID(customer_id)，顧客住所(address)，
# 店舗住所(address)とともに表示せよ．
# 計算式は以下の簡易式で良いものとするが，その他精度の高い方式を利用したライブラリを
# 使用しても構わない．
# 結果は10件表示せよ．
# 緯度(ラジアン): \phi
# 経度(ラジアン): \lambda
# 距離L = 6371 * arccos(sin \phi_{1} * sin \phi_{2} 
#         \cos \phi_{1} * cos \phi_{2} * cos(\lambda_{1} - \lambda_{2}))

import pandas as pd
import numpy as np

df_geocode = pd.read_csv("../data/geocode.csv", dtype={'prefecture':str, 'city':str, 'town':str, 'street':str, 'address':str, 'full_address':str})
df_customer = pd.read_csv("../data/customer.csv", dtype={'customer_id':str, 'customer_name':str, 'gender':str, 'gender_cd':str, 'address':str, 'application_store_cd':str})
df_store = pd.read_csv("../data/store.csv", dtype={'store_cd':str, 'store_name':str, 'prefecture':str, 'address':str, 'address_kana':str})

df_geocode_1 = df_geocode.groupby('postal_cd')\
		.agg(m_longitude=('longitude', 'mean'),
		     m_latitude=('latitude', 'mean')).reset_index()
df_customer_1 = pd.merge(df_customer, df_geocode_1, how='inner', on='postal_cd')

def calc_distance_numpy(x1, y1, x2, y2):
	x1_r = np.radians(x1)
	x2_r = np.radians(x2)
	y1_r = np.radians(y1)
	y2_r = np.radians(y2)
	return 6371 * np.arccos(np.sin(x1_r) * np.sin(x2_r)
		+ np.cos(x1_r) * np.cos(x2_r) * np.cos(y1_r - y2_r))

df_tmp = df_customer_1.merge(df_store, how='inner', left_on='application_store_cd', right_on='store_cd')\
		      .rename(columns={'address_x':'customer_address',
		      		       'address_y':'store_address'})

df_tmp['distance'] = calc_distance_numpy(df_tmp['m_latitude'],
					 df_tmp['m_longitude'],
					 df_tmp['latitude'],
					 df_tmp['longitude'])

ans86 = df_tmp[['customer_id', 'customer_address', 'store_address', 'distance']].head(10)

ans86.to_csv("../answer/ans86.csv")
#print(ans86)
