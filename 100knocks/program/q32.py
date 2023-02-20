##########
# q32.py #
##########
# レシート明細データ(df_receipt)の売上金額(amount)について，
# 25%刻みでパーセンタイル値を求めよ．

import pandas as pd
import numpy as np

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

ans32 = df_receipt.amount.quantile(q = np.arange(1, 5)/ 4)

ans32.to_csv("../answer/ans32.csv")
#print(ans32)
