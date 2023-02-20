##########
# q77.py #
##########
# レシート明細データ(df_receipt)の売上金額を顧客単位に合計し，合計した売上金額の外れ値を抽出せよ．
# なお，外れ値は売上金額合計を対数化した上で平均と標準偏差を計算し，
# その平均から3sigmaを超えて離れたものとする(自然対数と常用対数のどちらでも可)．
# 結果は10件表示せよ．

import pandas as pd
import numpy as np
from sklearn import preprocessing

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_sales_amount = df_receipt.groupby('customer_id').agg({'amount':'sum'}).reset_index()

df_sales_amount['log_sum_amount'] = np.log(df_sales_amount['amount'] + 0.5)
df_sales_amount['log_sum_amount_ss'] = preprocessing.scale(df_sales_amount['log_sum_amount'])

ans77 = df_sales_amount.query('abs(log_sum_amount_ss) > 3').head(10)

ans77.to_csv("../answer/ans77.csv")
#print(ans77)
