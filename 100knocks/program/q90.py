##########
# q90.py #
##########
# レシート明細データ(df_receipt)は2017年1月1日~2019年10月31日までのデータを有している．
# 売上金額(amount)を月次で集計し，学習用に12ヶ月，テスト用に6ヶ月の時系列モデル構築用データを
# 3セット作成せよ．

import pandas as pd
from sklearn.model_selection import TimeSeriesSplit

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_ts_amount = df_receipt[['sales_ymd', 'amount']].copy()
df_ts_amount['sales_ym'] = df_ts_amount['sales_ymd'].astype(str).str[0:6]
df_ts_amount = df_ts_amount.groupby('sales_ym').agg({'amount': 'sum'}).reset_index()

tscv = TimeSeriesSplit(gap=0, max_train_size=12, n_splits=3, test_size=6)

df_ts_amount = df_ts_amount.query('sales_ym <= "201906"')

series_list = []
for train_index, test_index in tscv.split(df_ts_amount):
	series_list.append((df_ts_amount.loc[train_index],
			    df_ts_amount.loc[test_index]))

df_train_1, df_test_1 = series_list[0]
df_train_2, df_test_2 = series_list[1]
df_train_3, df_test_3 = series_list[2]

df_train_1.to_csv("../answer/df_train_1.csv")
df_train_2.to_csv("../answer/df_train_2.csv")
df_train_3.to_csv("../answer/df_train_3.csv")
df_test_1.to_csv("../answer/df_test_1.csv")
df_test_2.to_csv("../answer/df_test_2.csv")
df_test_3.to_csv("../answer/df_test_3.csv")
