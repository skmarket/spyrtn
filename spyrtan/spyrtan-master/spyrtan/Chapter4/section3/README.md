# 4-3. リスト・タプル・辞書・集合

### 概要

section1 で Python でよく使うデータ型について見てきました。

1. 文字列 (str)
2. 整数 (int)
3. 浮動小数 (float)
4. 真偽値 (bool)
5. list
6. tuple
7. dict
8. set

ここでは5以降の

5. リスト list
6. タプル tuple
7. 辞書 dict
8. 集合 set

について詳しくみていきます。<br>

**リスト list**

配列です。<br>
一列にならべられた様子をイメージしてください。こちらの [京都産業大学　プログラミングβ 配列](http://www.cc.kyoto-su.ac.jp/~yamada/programming/array.html) の「配列とは」というのが参考になると思います。メモリの上に並んでいるんですね。

どのように宣言するかというと

```python
sample_list = [1, 2, 'a', 'b', True, False]
```

としてあげればOKです。<br>
この場合、メモリ上に順番に 1, 2, a, b, True, False が並んでいる様子をイメージしてください。<br>
ではこのリストから値を取り出してあげましょう。リストでは要素を先頭からの距離で指定します。つまり、最初の要素を取り出したいときは `print()` 関数を利用して

```python
print(sample_list[0])
```

としてあげればOKです。先頭から二番目の要素を指定したいときには

```python
print(sample_list[1])
```

となりますね。<br>
では次に値の更新をしてあげましょう。３番目の `'a'` を `'あ'` に変更してみましょう。

```python
sample_list[2] = 'あ'
```

としてあげればOKです。


**タプル　tuple**

さて次はタプルです。宣言の方法は

```python
sample_tuple = (1, 2, 'a', 'b', True, False)
```

といった感じです。list と同じように見えますね。
値の取得も

```python
print(sample_tuple[0])
```

としてあげれば、最初の値を取り出すことができます。<br>
それでは次に値の更新をしてあげましょう。

```python
sample_tuple[1] = 20
```

あれ、TypeError (データ型に関するエラー) になってしまいましたね ...<br>
そうなんです。タプルは imutable (イミュータブル) なデータ型なのです。<br>
対して、リストはミュータブルなデータ型です。この２つの実用上の違いというのは後々みていくことにしましょう。（オブジェクトという概念を理解する必要があるので後回しにしています。）<br>
現段階では、「リストは要素を書き換えられるが、タプルは書き換えられない。」という理解でバッチリかと思います。

**集合 set**

先に集合を見ていきましょう。<br>
集合は、重複を許さない配列です。まさしく数学の集合ですね。

```python
sample_set = {1, 2, 3, 4}
```

のように宣言します。<br>
また、仮に

```python
sample_set = {1, 2, 3, 4, 4, 4}
```

というように宣言しても

```python
print(sample_set)
```

で,  `{1, 2, 3, 4}` となっていることが確認できるかと思います。<br>
集合演算が定義されているので、（積集合・和集合・差集合など）集計などで活躍するデータ型となります。

**辞書　dict**

さて、最後は辞書型です。<br>
辞書型はその名の通り、キーとバリューのペアになっています。（単語と説明みたいな感じですね）

```python
sample_dict = {'a': 'あ', 'b': 'い'}
```

というように宣言します。また、基本的にキーを指定することでバリューを取得します。（単語を探して、説明を読むような感じですね。）<br>
うえの例で、'a' に対応する値を取得するためには、

```python
print(sample_dict['a'])
```

のようにしてあげます。<br>
ざっと概要を抑えることができたので、リストと辞書だけ詳しく見ていきましょう。



### リスト

ここでは、リストに用意されている関数についてよく使うものを紹介します

1. `len`

リストの要素数を取得できます。

```python
sample_list = [1, 2, 3, 4]
print(len(sample_list)) # expected: 4
```

2. `append`

リストに要素を追加する際に利用します。<br>
`+=` などを使っても要素を追加できますが、コードを読んでいてわかりやすいのでこちらがおすすめです。

```python
sample_list = [1, 2, 3, 4]
sample_list.append(5)
print(sample_list) # expected: [1, 2, 3, 4, 5]
```

sample_list という変数のあとに `.` をつけたあとに関数 `append()` を宣言することに注意してください。（これにもやっとした方、 section5 で解決するのでご安心ください！）


3. `pop`, `remove`

どちらも要素を削除できる関数です。<br>
`pop` は指定した位置の要素を削除し、その要素を取得できます。<br>
`remove` は指定した値を削除します


```python
sample_list = [1, 2, 3, 4]
result1 = sample_list.pop(0)
print(result) # expected: 1
print(sample_list) # expected: [1, 2, 3]

sample_list.remove(4)
print(sample_list) # expected: [2, 3]
```

といった感じですね。他にもたくさん関数が用意されています。<br>
Python のリファレンスとしてかなり有用な note.nkmk.me でまとめられているので、興味があるものがあれば見てみてください。<br>
[note.nkmk.me Top > リスト](https://note.nkmk.me/list/)


### 辞書

さて、辞書についてもよく使う関数を見ていきましょう。

1, `keys`

定義した辞書のキーを `dict_keys` クラスとして返します。（クラスは section5 でやります）<br>
リストへキャスト（型変換）するための `list()` 関数を利用することで、辞書のキーをリストとして取得することができます

```python
location = {
    'さいたま': 'a',
    '赤羽': 'b',
    '横浜': 'a'
}

print(list(location.keys()))
```

2, pop

`pop` は指定したキーに対応する要素を削除し、そのバリューを取得できます。

```python
location = {
    'さいたま': 'a',
    '赤羽': 'b',
    '横浜': 'a'
}

rank_saitama = location.pop('さいたま')
print(rank_saitama) # expected: 'a'
print(location) # expected: {'赤羽': 'b', '横浜': 'a'}
```

こちらも note.nkmk.me でまとまっていますのでご覧ください。<br>
[note.nkmk.me Top > 辞書](https://note.nkmk.me/dictionary/)


### 関数の可変長引数

さて、リスト、タプル、集合や辞書についてみてきました。<br>
実は、タプルと辞書は関数の引数とも関係しています。

それは、可変長引数というものです。<br>
たとえば、ある人がしたキー入力を順番に受け取る関数を考えます。

```python
def key_input():
    pass
```

ここで、関数の外と関数の中をつなぐのが仮引数でした。<br>
しかし、キー入力は長さがきまっていません。<br>
どうしたらいいでしょう ...実引数が

```python
key_input('a', 'p', 'p', 'l', 'e')
```

かもしれませんし、

```python
key_input('b', 'l', 'u', 'e')
```

かもしれません。困りました。<br>
そんなときに役に立つのが可変長位置引数です。 `*` を利用することで、任意の数の実引数を位置引数として取得できます。

```python
def key_input(*key_inps):
    print(key_inps)
    print(type(key_inps))
```

これを apple と blue それぞれの例で実行してみてください。引数がタプルとして `key_inps` 変数に格納されているのが分かるかと思います。また、可変長位置引数は、通常の位置引数より後ろにある必要があります。

```python
def key_input(first, *other_inps):
    pass
```

はOKですが、

```python
def key_input(*inps, last):
    pass
```

はNGということですね。<br>
もう１つ任意の数のキーワド引数を取得する方法として、可変長キーワド引数というものがあります。これは `**` を使います。

たとえば、ある人が食べたフードに対してランク付けしたものを処理することを考えてみましょう。

```python
def food_rank(**user_response):
    pass

# a さんの評価
food_rank(banana='a', lemon='c')

# a さんの評価
food_rank(banana='a', tea='c')
```

このように、任意のキワード引数を処理することができます。ちなみにこの可変長キーワード引数は辞書型です。

難しく見えますが使えると便利なので抑えておきましょう。

ここまできたら、quiz.py を解いてみましょう！
