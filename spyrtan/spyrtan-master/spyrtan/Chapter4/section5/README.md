# 4-5. 関数・引数

### オブジェクト指向とは

最後にオブジェクト指向についてみていきましょう。<br>
といってもなかなか一筋縄ではいかない概念です。<br>
今すぐに理解できなくても問題ないですし、コードを書く中でだんだんわかってくるものだったりします。

「オブジェクト指向　わかりやすく」などとググるとたくさん記事が出てくると思いますので、まず分かりやすそうなのを読んでみてください。<br>

- クラス
- インスタンス変数・クラス変数
- メソッド
- 継承
- インスタンス

あたりの言葉がなんとなくイメージできればOKかと思います。<br>
ざっくりと説明すると、

- クラス
いくつかの具体的な事象を抽象化したデータ型です。<br>
共通するデータやふるまいを定義することができます

- インスタンス変数・クラス変数
クラスがもつ共通するデータのこと

- メソッド
クラスがもつ共通するふるまいのこと

- 継承
いくつかのクラスについて共通する事象を抽象化したものを用意し、クラスの共通の親として呼び出すこと。

- インスタンス
クラスから生成された具体的な事象

といった感じです。<br>
百聞は一見に如かず、早速見ていきましょう。

---

### クラスの定義

それではクラスを定義していきます。<br>
今welcome メール: 新規登録した人に送るメール

```python
welcome_info = {
    'to': 'user@email.com',
    'from': 'kondo@comp.ja'
}

welcome_body = '登録いただきありがとうございます'

welcom_img = 'welcome.png'

def send_welcome(welcome_info, welcome_body, welcom_img):
    """
    mail を送信する
    send() という関数はすでに実装されているものとする
    """
    send(
        data = (welcome_info, welcome_body),
        header_img = welcom_img
    )

send_welcome(welcome_info, welcome_body, welcom_img)
```

というような実装があるとします。<br>
情報をそれぞれ変数に格納して、送信する関数を別途用意して処理をまとめている感じです。

ここで welcome メールだけでなく商品購入のお礼メールを送ることになりました。<br>
送信の処理は関数で共通化できそうだったので、名前を `send_mail` にしています。

```python
welcome_info = {
    'to': 'user@email.com',
    'from': 'kondo@comp.ja'
}
welcome_body = '登録いただきありがとうございます'
welcom_img = 'welcome.png'

thanks_info = {
    'to': 'user@email.com',
    'from': 'kondo@shop.ja'
}
thanks_body = '購入いただきありがとうございます'
thanks_img = 'thanks.png'

def send_mail(info, body, img):
    """
    mail を送信する
    send() という関数はすでに実装されているものとする
    """
    send(
        data = (info, body),
        header_img = img
    )

if send_welcom_mail:
    send_mail(welcome_info, welcome_body, welcom_img)
elif send_thanks_mail:
    send_mail(thanks_info, thanks_body, thanks_img)
```

これまで勉強した関数による処理の共通化や、関数や変数の命名に気を付けたコードになっていますね。<br>
ただ、これは welcome メールと thanks メールという２つの具体的な要素を別々に実装していることになります。

クラスはこの２つを抽象化することができます。

ではこの２つを観察して共通の要素を見つけましょう

- どちらも `info, body, img` という「データ」をもつ
- どちらも `send_mail` という「ふるまい」をもつ

ではこれらをもつ Mail クラスを定義してみましょう。

```python
class Mail:
    pass
```

というように宣言します。まずはデータについて定義しましょう。<br>
コンストラクタ関数 `__init__` を利用して指定することができます

```python
class Mail:
    
    def __init__(self, info, body, img):
        self._info = info
        self._body = body
        self._img = img
```

Mail クラスは、self で Mail クラス自身を指すことができます。<br>
つまり、`self._info` は Mail クラスの `_info` インスタンス変数ということです。<br>
`__init__` の仮引数である `info` でうけとった値を代入していますね。

一旦話を進めてしまいます。<br>
ふるまいを定義していきましょう

```python
class Mail:

    def __init__(self, info, body, img):
        self._info = info
        self._body = body
        self._img = img

    def send_mail(self):
        """
        mail を送信する
        send() という関数はすでに実装されているものとする
        """
        send(
            data = (self._info, self._body),
            header_img = self._img
        )
```

このように Mail クラスに `send_mail` 変数を作成することができます。<br>
メソッドには `self` という変数を仮引数として渡す必要があります。そして、この `self` によってメソッド内で `__init__` （コンストラクタ）で指定したインスタンス変数にアクセスすることができるのです。

さぁ最後にこれらのインスタンスを取得してあげましょう。<br>
まず、welcome メールのインスタンスを作成し、メールを送信してみます。

```python
class Mail:
    
    def __init__(self, info, body, img):
        self._info = info
        self._body = body
        self._img = img

    def send_mail(self):
        """
        mail を送信する
        send() という関数はすでに実装されているものとする
        """
        send(
            data = (self._info, self._body),
            header_img = self._img
        )

welcome_mail = Mail(
    info = {
        'to': 'user@email.com',
        'from': 'kondo@comp.ja'
    },
    body = '登録いただきありがとうございます'
    img = 'welcome.png'
)
welcome_mail.send_mail()
```

となります。 `Mail()` としてインスタンスを作成することができます。<br>
その際に、`__init__` (コンストラクタ) が実行されるので、指定した引数を渡すことができます。<br>
今回は、`info, body, img` を指定していますね。

また、インスタンスの後に `.` をつけることでクラス内のインスタンス変数やメソッドを利用できることも押さえておきましょう。<br>
今回は、`welcome_mail` というインスタンスに `.` をつけて `send_mail()` というクラス内のメソッドを呼び出しています。


では同様に thanks メールについてもインスタンスを作成し、送信してみましょう。

```python
class Mail:
    
    def __init__(self, info, body, img):
        self._info = info
        self._body = body
        self._img = img

    def send_mail(self):
        """
        mail を送信する
        send() という関数はすでに実装されているものとする
        """
        send(
            data = (self._info, self._body),
            header_img = self._img
        )

welcome_mail = Mail(
    info = {
        'to': 'user@email.com',
        'from': 'kondo@comp.ja'
    },
    body = '登録いただきありがとうございます'
    img = 'welcome.png'
)
welcome_mail.send_mail()

thanks_mail = Mail(
    info = {
        'to': 'user@email.com',
        'from': 'kondo@shop.ja'
    },
    body = '購入いただきありがとうございます'
    img = 'thanks.png'
)
thanks_mail.send_mail()

```

このようにメールが増えても、簡単に実装することができます。<br>
また、メールについて変更を加えたい場合も Mail クラスだけをみればいいので保守性が高くなります。

ざっとでしたが、このように具体的な実装をクラスに抽象化することができます。

---

### Python はすべてオブジェクトである

さぁ最後に衝撃的な事実です。<br>
Python ではすべてのデータ型がオブジェクトとして実装されています。

つまりすべてクラスをもつということです。

```python
sample_sentence = 'abc'
```

とすると内部的には String クラスのインスタンスが作成されるといった感じです。<br>
なので、`sample_sentence.split('b')` というような処理が可能になるんですね。これは String クラスの `split()` というメソッドにアクセスしています。

そしてこれから使用していくライブラリなんかも当然オブジェクトです。<br>
コードを書きながらオブジェクト指向がどういうものかなんとなく理解していきましょう。

それでは quiz.py へ進んでください！
