##########
# q74.py #
##########
# レシート明細データ(df_receipt)の売上日(sales_ymd)に対し，
# 当該週の月曜日からの経過日数を計算し，売上日，直前の月曜日付とともに10件表示せよ．
# sales_ymdは数値でデータを保持している点に注意．

import pandas as pd
from dateutil.relativedelta import relativedelta

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_tmp = df_receipt[['sales_ymd']].copy()

df_tmp['sales_ymd'] = pd.to_datetime(df_tmp['sales_ymd'].astype(str))
df_tmp['elapsed_days'] = df_tmp['sales_ymd'].apply(lambda x: x.weekday())
df_tmp['monday'] = df_tmp['sales_ymd'].apply(lambda x: x - relativedelta(days=x.weekday()))

ans74 = df_tmp.head(10)

ans74.to_csv("../answer/ans74.csv")
#print(ans74)
