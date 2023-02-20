##########
# q99.py #
##########
# q93で作成したカテゴリ名付き商品データを以下の仕様でファイル出力せよ．
# |ファイル形式|ヘッダ有無|文字エンコーディング||:--:|:--:|:--:||TSV(カンマ区切り)|有り|UTF-8|
# ファイル出力先のパスは以下のようにすること．
# |出力先||:--:||./data|

import pandas as pd

df_product_full = pd.read_csv('../answer/ans93.csv',
				sep='\t', encoding='UTF-8', header=None)

ans99 = df_product_full

ans99.to_csv("../answer/ans99.tsv")
#print(ans99)
