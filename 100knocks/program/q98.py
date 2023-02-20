##########
# q98.py #
##########
# q96で作成した以下形式のファイルを読み込み，データを3件表示させて
# 正しく取り込まれていることを確認せよ．
# |ファイル形式|ヘッダ有無|文字エンコーディング||:--:|:--:|:--:||CSV(カンマ区切り)|ヘッダ無し|UTF-8|

import pandas as pd

df_product_full = pd.read_csv('../answer/ans96.csv',
				dtype={1:str,
				       2:str,
				       3:str},
				encoding='UTF-8', header=None)

df_product_full.columns = ['product_cd', 
			   'category_major_cd',
			   'category_medium_cd',
			   'category_small_cd',
			   'unit_price',
			   'unit_cost',
			   'category_major_name',
			   'category_medium_name',
			   'category_small_name']
			   
ans98 = df_product_full.head(3)

ans98.to_csv("../answer/ans98.csv")
#print(ans98)
