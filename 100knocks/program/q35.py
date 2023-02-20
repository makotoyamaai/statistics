##########
# q35.py #
##########
# レシート明細データ(df_receipt)に対し，顧客ID(customer_id)ごとに
# 売上金額(amount)を合計して全顧客の平均を求め，平均以上に買い物をしている
# 顧客を抽出し，10件表示せよ．
# ただし，顧客IDが"Z"から始まるものは非会員を表すため，除外して計算すること．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

df_amount_sum = df_receipt.query('not customer_id.str.startswith("Z")', engine='python').groupby('customer_id').amount.sum()
amount_mean = df_amount_sum.mean()
df_amount_sum = df_amount_sum.reset_index()
ans35 = df_amount_sum[df_amount_sum['amount'] >= amount_mean].head(10)

ans35.to_csv("../answer/ans35.csv")
#print(ans35)
