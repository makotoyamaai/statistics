##########
# q51.py #
##########
# レシート明細データ(df_receipt)の売上エポック秒(sales_epoch)を日付型に変換し，
# 「日」だけ取り出してレシート番号(receipt_no)，レシートサブ番号(receipt_sub_no)
# とともに10件表示せよ．
# なお，「日」は0埋め2桁で取り出すこと．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype={'store_cd':str, 'customer_id':str, 'product_cd':str})

df_datetime = pd.to_datetime(df_receipt['sales_epoch'], unit='s').rename('sales_day')

ans51 = pd.concat([df_receipt[['receipt_no', 'receipt_sub_no']],
			       df_datetime.dt.strftime('%d')], axis=1).head(10)

ans51.to_csv("../answer/ans51.csv")
#print(ans51)
