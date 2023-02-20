##########
# q19.py #
##########
# レシート明細データ(df_receipt)に対し，1件あたりの売上金額(amount)が高い順にランクを付与し，
# 先頭から10件表示せよ．
# 項目は顧客ID(customer_id)，売上金額(amount)，付与したランクを表示させること．
# なお，売上金額(amount)が等しい場合は同一順位を付与するものとする．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_id':str, 'customer_id':str, 'product_id':str})

df_tmp = pd.concat([df_receipt[['customer_id', 'amount']], df_receipt['amount'].rank(method='min', ascending=False)], axis=1)

df_tmp.columns = ['customer_id', 'amount', 'ranking']

ans19 = df_tmp.sort_values('ranking').head(10)

ans19.to_csv("../answer/ans19.csv")
#print(ans19)
