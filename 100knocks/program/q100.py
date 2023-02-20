###########
# q100.py #
###########
# q99で作成した以下形式のファイルを読み込み，データを3件表示させて
# 正しく取り込まれていることを確認せよ．
# |ファイル形式|ヘッダ有無|文字エンコーディング||:--:|:--:|:--:||TSV(タブ区切り)|有り|UTF-8|

import pandas as pd

df_product_full = pd.read_csv('../answer/ans99.tsv',
				dtype={'category_major_cd':str,
				       'category_medium_cd':str,
				       'category_small_cd':str},
				sep='\t', encoding='UTF-8')

ans100 = df_product_full.head(3)

ans100.to_csv("../answer/ans100.tsv")
print(ans100)
