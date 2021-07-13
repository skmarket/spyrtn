# -*- coding: utf-8 -*-

import json
import requests
from http import HTTPStatus
# ref: pprint -> https://note.nkmk.me/python-pprint-pretty-print/
from pprint import pprint


"""
[問題１]
入力された文字列が回文かどうかをチェックする関数を作りたいです。

回文というのは
https://ja.wikipedia.org/wiki/%E5%9B%9E%E6%96%87

- しんぶんし
- はかなの世しばしよしばし世の中は（はかなのよしはしよしはしよのなかは）

というようなものです。
これらの文章を sentence という引数で受け取り、回文であれば True を
回文でなければ False を返すような関数 palindrome を作成してください。

余裕のある方は、docsting で関数の説明をつけてみてください
https://qiita.com/11ohina017/items/118b3b42b612e527dc1d
"""
def palindrome(sentence):
    pass



"""
[問題２]

Qiita の Python に関する検索を返す関数 search_qiita を用意しました。
この関数は辞書型のデータを返します。

search_qiita 関数を実行して返される辞書型のデータの構造を確認してください。
参考: https://qiita.com/api/v2/items?query=python

pprint 関数を使うと整形して表示することができます。
"""
def search_qiita(num_record=50, query='python'):
    """Qiita API v2 から Python に関する記事を返す関数

    :params
        num_recoerd: int

    :return
        Qiita API を叩いた結果の Json を dict に変換したもの
    """
    url = f'https://qiita.com/api/v2/items?query={query}&per_page={num_record}'
    res = requests.get(url)
    if res.status_code == HTTPStatus.OK:
        return json.loads(res.text)
    else:
        Exception('データの取得に失敗しました')
        exit(10)


"""
[問題３]

search_qiita を利用して、記事のタイトルのみを表示させる関数
show_title を作成してください

出力例
```
Python 3 エンジニア認定データ分析試験受験前学習について
Python 3 エンジニア認定データ分析試験の4つのライブラリを勉強してみた
zsh: command not found: jupyterの対応
【自動化】PythonでOutlookの予定を抜き出す
FastAPI vs Vert.x　ベンチマークとか感想とか
Django Signalsの種類と使い方
Chainerによる機械学習のためのPython学習メモ　13章 ニューラルネットワークの基礎
Twitter Botで引用RTをするときにつまづいたメモ
python:3.8-alpineでException: you need a C compiler to build uWSGIエラーへの対処
yukicoder contest 271 参戦記
(省略)
```
"""

def show_title():
    pass



"""
[問題４]

search_qiita を利用して、取得されるデータのうち
tag の情報を集計したいです。

全ての記事についているタグの名前(name)を**重複なく**表示させてください。

tag がどのように記載されているかについては
https://qiita.com/api/v2/docs#get-apiv2items
に記載されている json の例を参考にしてください

出力例
```
notebook,
AtCoder
Linuxコマンド
C++
Twitter
アルゴリズム
Python3
疑似コード
ソートアルゴリズム
シナリオ
RStudio
sam
MetricFire
(省略)
```
"""

def show_tag():
    pass


"""
[問題5]

follower の多い人が書いた上位 10 記事を表示させたいです。
search_qiita を利用して、上位 10 記事のそれぞれについて

- title: 記事のタイトル
- link: リンク
- num_follwer: follower の数

をキーに、値をバリューにもつ辞書型のデータを格納して、
それぞれの記事をリスト型に格納してください。

そのリストを返り値とする関数 pick_top_5 を実装してください

返り値の例
```
[
    {
        'title': 'python 初めてみました',
        'link': https://hogehoge.com,
        'num_follwer': 10324
    },
    {
        'title': 'python 大好き',
        'link': https://hogehoge.com,
        'num_follwer': 6000
    },
    {
        'title': 'python のコツ',
        'link': https://hogehoge.com,
        'num_follwer': 200
    },
    (省略)
]
```
"""
def pick_top_5():
    pass



"""
[問題６]

pick_top_5 の返り値を利用して以下のような文字列型に整形して出力する関数
print_record を作成しましょう

ただし、print 関数は print_record 内で一度のみ実行するものとします

出力する文字列
```
今日の記事 top 10

---- 01 ---
タイトル: python 初めてみました
link: https://hogehoge.com

--- 02 ---
タイトル: python 大好き
link: https://hogehoge.com

(中略)

--- 10 ---
タイトル: python 大好き
link: https://hogehoge.com
```
"""

def print_record():
    pass


"""
[問題７]


実は search_qiita 関数は query 引数に好きなキーワードを入れると
その単語について検索できます。

今日のあるキーワードについて、ご自身で基準を設定して記事とリンクを表示
させてみましょう

- follwer の数
- そのユーザーの書いた記事の数
- 最新のものから順に

など色々できます
どんな情報が取得できるかは
https://qiita.com/api/v2/docs#get-apiv2items
を参照してください


より関数を再利用しやすい形にすることを意識して、実装してみましょう !
"""
