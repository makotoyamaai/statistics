##########
# q48.py #
##########
# レシート明細データ(df_receipt)の売上エポック秒(sales_epoch)は数値型のUNIX秒で
# データを保有している．これを日付型に変換し，レシート番号(receipt_no)，
# レシートサブ番号(receipt_sub_no)とともに10件表示せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

ans48 = pd.concat([df_receipt[['receipt_no', 'receipt_sub_no']],
		   pd.to_datetime(df_receipt['sales_epoch'], unit='s').rename('sales_ymd')],
		  axis=1).head(10)

ans48.to_csv("../answer/ans48.csv")
#print(ans48)
