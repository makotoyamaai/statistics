##########
# q31.py #
##########
# レシート明細データ(df_receipt)に対し，店舗コード(store_cd)ごとに
# 売上金額(amount)の標準偏差を計算し，降順で5件表示させよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans31 = df_receipt.groupby('store_cd').amount.std(ddof=0).reset_index().sort_values('amount', ascending=False).head(5)

ans31.to_csv("../answer/ans31.csv")
#print(ans31)
