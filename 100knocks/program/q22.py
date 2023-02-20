##########
# q22.py #
##########
# レシート明細データ(df_receipt)の顧客ID(customer_id)に対し，ユニーク件数をカウントせよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans22 = len(df_receipt['customer_id'].unique())

data = {'unique':[ans22]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans22.csv")
#print(ans22)
