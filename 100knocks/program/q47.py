##########
# q47.py #
##########
# レシート明細データ(df_receipt)の売上日(sales_ymd)はYYYYMMDD形式の数値型でデータを保有している．
# これを日付型に変換し，レシート番号(receipt_no)，レシートサブ番号(receipt_sub_no)とともに
# 10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

ans47 = pd.concat([df_receipt[['receipt_no', 'receipt_sub_no']],
		   pd.to_datetime(df_receipt['sales_ymd'].astype(str))],
		  axis=1).head(10)

ans47.to_csv("../answer/ans47.csv")
#print(ans47)
