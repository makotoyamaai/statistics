##########
# q21.py #
##########
# レシート明細データ(df_receipt)に対し，件数をカウントせよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans21 = len(df_receipt)

data = {'len':[ans21]}
ans_data = pd.DataFrame(data)

ans_data.to_csv("../answer/ans21.csv")
#print(ans21)
