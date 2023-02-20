##########
# q34.py #
##########
# レシート明細データ(df_receipt)に対し，顧客ID(customer=id)ごとに
# 売上金額(amount)を合計して全顧客の平均を求めよ．
# ただし，顧客IDが"Z"から始まるものは非会員を表すために，除外して計算すること．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans34 = df_receipt.query('not customer_id.str.startswith("Z")', engine='python').groupby('customer_id').amount.sum().mean()

data = {'mean':[ans34]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans34.csv")
#print(ans34)
