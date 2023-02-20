##########
# q30.py #
##########
# レシート明細データ(df_receipt)に対し，店舗コード(store_cd)ごとに
# 売上金額(amount)の分散を計算し，降順で5件表示させよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans30 = df_receipt.groupby('store_cd').amount.var(ddof=0).reset_index().sort_values('amount', ascending=False).head(5)

ans30.to_csv("../answer/ans30.csv")
#print(ans30)
