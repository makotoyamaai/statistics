##########
# q49.py #
##########
# レシート明細データ(df_receipt)の売上エポック秒(sales_epoch)を日付型に変換し，
# 「年」だけ取り出してレシート番号(receipt_no)，レシートサブ番号(receipt_sub_no)
# とともに10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

ans49 = pd.concat([df_receipt[['receipt_no', 'receipt_sub_no']],
		   pd.to_datetime(df_receipt['sales_epoch'], unit='s')\
		   .dt.year.rename('sales_year')],
		  axis=1).head(10)

ans49.to_csv("../answer/ans49.csv")
#print(ans49)
