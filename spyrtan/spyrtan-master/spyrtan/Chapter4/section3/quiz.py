import pandas as pd
import os
import pathlib
import pprint.pprint as pprint

"""
e-stats から 2013 年の企業のワーク・ライフ・バランスに関する調査
https://www.e-stat.go.jp/dbview?sid=0003346052

について、データを辞書型に変換する関数 fetch_data を用意しました。
（元データは、section3 ディレクトリの data.csv です)
"""

def fetch_data():
    f_path = pathlib.Path(__file__).joinpath('../data.csv') 
    worklife_df = pd.read_csv(f_path, header=1)
    return worklife_df.to_dict()


"""
[問題１]

data.csv と e-stats をみて、どのようなデータなのか理解しましょう。
次に fetch_data 関数によって返される辞書を取得し、その辞書がどのような構造か調査してください。
辞書の要素を調査するときには pprint 関数を利用すると便利です

そして、支所数ごとの回答企業数を出力する show_comp 関数を作成しましょう
以下のような出力がされればOKです

期待される出力

支所数\t数値[社]

```
全体    1016社
0箇所   114社
１～５か所  302社
６〜１０箇所    234
１１〜２０箇所  208
...
```
"""

def show_comp():
    pass

"""
[問題２]

問題１の表示について、「全体」をのぞき回答数が多い順に並び変えて表示させてください
別途 show_sorted_comp という関数を作成するものとします

"""

def show_comp():
    pass



"""
[問題３]
支所数が 11 箇所以上ある会社を大企業とします
大企業で、残業時間が 50 時間を超えている会社の数をもとめてください

"""



"""
[問題４]
業務の効率を計測するために、以下のような指標を考えました

効率 = 進んだ作業量 / 作業時間

効率を向上させるにあたり、作業時間の削減を目標にしています。
残業時間を引数としてうけとり、その時間以上の残業をしている
会社の数を出力する monitor 関数を作成しましょう。

この時、対象は全社とします。
また、力試しをしたい方は

- 全体
- 大手企業: 支所数 11 箇所
- 中小企業: 支所数 1 箇所以上 10 箇所以下
- ベンチャー企業: 支所数 0 箇所

を関数の引数として指定することで、結果を出しわけられるようにしてみましょう。
"""

def monitor(overtime):
    pass


"""
[問題 5]
monitor を copy して、moniter_with_option 関数を作成してください。
ご自身であらたな処理を考えてオプションを付けてみましょう。

たとえば、結果の出力を派手に装飾する illust オプションをつけるなら

monitor_with_option(overtime, illust=False):
    ”””
    指定された時間以上の残業をしている会社の数を表示する
    :params
        overtime: 残業時間 (時間)
        illust: True の時結果を派手に装飾する 
    ”””
    ...
    num_company = ...

    if illust:
        print(f"*+*+*+*+*+ {num_company} 社 +*+*+*+*+*+*")
    else:
        print(f"{num_company} 社")

という感じです。
余裕のある方は、オプションを複数用意し可変長キーワード引数を利用してみましょう
"""

