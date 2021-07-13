# 3-2. Python の実行方法

さぁ。ようやく Python を実行させてみましょう。<br>
Python には 2 通りの実行方法があります。

- 対話型インタープリター形式
- ファイルでの実行

です。

---

### 対話型インタプリタとしての起動

では、まずは対話型インタプリタ形式で実行していきましょう。<br>
コードの挙動を確かめるときなど、かなり小規模なプログラムを実行するときに利用することが多いです。

では、Windows であれば GitBash を起動して、

```shellscript
python
```

macOS であれば terminal を起動して

```shellscript
python3
```

と入力しましょう。<br>
すると

```shellscript
Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

のような感じで対話型インタプリタというものが起動します。<br>
ここに

```shellscript
>>> print('hello')
```

と入力すると

```shellscript
>>> print('hello')
hello
```

とすぐに結果が返ってきたと思います。<br>
このように、すぐに結果が返ってくるので「対話型」インタープリターと呼ばれます。

慣れない頃は挙動を確かめながら動かせるので便利です。<br>
`exit()` と入力することで終了することができます。

しかし、この対話型インタープリタは一度終了するとそれまでの処理はすべて忘れてしまいます。<br>
そこで、ファイルでの実行が必要になるのです。

---

### ファイルでの実行

ファイルでの実行は、あらかじめ Python のコードをファイルに書いておき実行する方法です。<br>
では、Spyrtan 用のディレクトリ配下に `python_startup` というディレクトリを作りましょう。<br>
`python_startup` に移動します。（ここも Unix Command でさらっとできると Good ですね。）

では、`python_startup` の配下に、`start_up.py` という Python ファイルを作成します。<br>
`.` の後を拡張子と呼び、ファイルの種類を特定するのに用いるものです。Python ではこれに `.py` を指定します。<br>
では、ファイルの中に Python のコードを書いていきましょう。

```python
print('hello')
```

これでファイルの準備は完了です。<br>
VSCode の Terminal から。新しいターミナルを起動しましょう。

`ls` で `start_up.py` があることを確認し、実行してみましょう。

Windows であれば

```shellscript
python start_up.py
```

macOS であれば

```shellscript
python3 start_up.py
```

と実行します。<br>

```shellscript
hello
```

と表示されれば成功です！おめでとうございます :rocket:

ここまでできたら次のセクションに取り組んでみましょう。
