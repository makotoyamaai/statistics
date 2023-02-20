#########
# q1.py #
#########
# レシート明細データ(df_receipt)から全項目の先頭10件を表示し，
# どのようなデータを保有しているか目視で確認せよ．

import pandas as pd

df_receipt = pd.read_csv("../data/receipt.csv", dtype=str)

ans1 = df_receipt.head(10)

ans1.to_csv("../answer/ans1.csv")
#print(ans1)
