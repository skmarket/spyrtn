# 2-3. Unix コマンド

### Windows10 のための bash

macOS ではデフォルトで Unix コマンドが使えるのですが、Windows では使えません。<br>
独自のコマンドが用意されているのですが、Unix コマンドのほうがプログラミングをする上では一般的であったり、資料がたくさんあったりするので Unix コマンドを使う準備をしていきましょう。

https://qiita.com/taketakekaho/items/75161e1273dca98cb4e1

上の資料を参考に、Git Bash を起動してみましょう。<br>
次に前のセクションで準備した VSCode でも Unix Command をつかえるようにしましょう。

https://qiita.com/y_marito/items/22ffd8c28119066c47f6

こちらの記事で Git Bash を VSCode に導入することができます。<br>
ここまでで、 Unix コマンドを使う準備が整いました！ここからは Unix コマンドについて勉強していきましょう。

---

### Unix Command とは何か

まずは Unix Command とは何かを理解するところから始めましょう。<br>
Unix コマンドは Unix 系の OS を操作するためのコマンドです。

Unix 系というように、Unix の考えに基づいた OS はいくつかあります。<br>
代表的なもので言うと、

- Linux
- macOS

です。

そして、「操作する」と言いましたが一般的な画面をポチポチする GUI （グラフィカルユーザーインターフェース）と異なり、<br>
CLI （コマンドラインインターフェース）と呼ばれる方法で操作します。

よく見る黒い画面に白い文字でハッカーがカタカタしている絵は、CLI を利用して PC を操作しています。<br>
まとめると、Unix 系のコンピュータをコマンドラインで操作するためのツールが　Unix コマンドです。

---

### Unix Command をなぜ使うのか

とはいえ、普通に GUI を使う方が楽そうですよね…<br>
エンジニアを目指すわけではないみなさんが CLI を使った方がいい理由としては

- 開発が早くなる
- 開発の選択肢を増やし、楽に開発できる

といったところでしょうか。<br>
急がば回れとはまさにその通りで、CLI を使えることようになることがプログラミング上達の役に立ちます。

きっとこの勉強の後半には、 「CLI 便利だわー」 となっていると思いますので頑張って使っていきましょう :rocket:

---

### よく使う Unix Command

ただ、いざ始めようと思っても Unix Command はとてもたくさんあるので全てを使えるようになるのは大変です。<br>
そこでよく使うものに絞ってご紹介します。

ちなみに Unix Command に限らずですが、CLI では

```shellscript
Command command_arg
```

といった並びになることが多いです。<br>
Command を実行し、そのコマンド実行に必要な情報を引数（argument） として渡します。<br>
引数は0個だったり、複数あったりします。

#### pwd

Print Working Directory の略で、現在見ているディレクトリのホームディレクトリから見たパスを教えてくれます。<br>
(`>` の行では出力例を表しています。)

```shellscript
pwd
> /Users/motoya_kondo
```


#### ls

Look source の略で、カレントディレクトリに存在するファイルやディレクトリの一覧を見ることができます。<br>
(期待される出力はワーキングディレクトリがどこか、そこにどのようなファイルやディレクトリがあるかに依存します。出力はこの通りではありません。)

```shellscript
ls
> Applications               Library               Movies               SQLServer               Desktop               Download
```

#### cd

Change Dorectory の略で、ディレクトリを移動することができます。

```shellscript
cd Desktop
```

#### mkdir 

ディレクトリを作成することができます。

```shellscript
mkdir sample_dir
```

上のコマンドを実行すると、新しく sample_dir というディレクトリが生成されています。<br>
`ls` で確認してみましょう！　そして `cd` を利用して `sample_dir` に移動し、 `pwd` で移動できたことを確認してみましょう。

#### touch

空のファイルを作成する方ができます。

```shellscript
touch sample.txt
touch .kakushi_file
```

`ls` で `sample.txt` が生成されていることを確認してみましょう。<br>
`.` から始めるファイルは隠しファイルと呼ばれ、システムにとって重要な情報を保持していたりしてユーザー側からは見れなくなっています。<br>
そのため `.kakushi_file` は `ls` では表示されません。

#### rm

remove の略で、ファイルやディレクトリの削除に利用します。

```shellscript
rm sample.txt
```

`ls` で `sample.txt` が削除されていることを確認してみましょう。


#### オプション

オプションを指定することによって、コマンドの動作を少し変えることができます。<br>
基本的にオプションは

```shellscript
Command --option option_arg command_arg
```

というような形で指定されます。<br>
例えば、ls に対して、隠しファイルも含めた全てのファイルを表示してみましょう

```shellscript
ls --all 
```

というようにすれば OK です。<br>
こうすると先ほどは見えなかった `.kakushi_file` が見えるようになったかと思います。<br>
ちなみに `--all` と書くのは面倒なので、よく使うオプションには省略形が用意されています。

```shellscript
ls -a 
```

としても同じように動作することを確認してみましょう。<br>
さらに複数のオプションを同時に指定することもできて

```shellscript
ls -la 
```

とすると、隠しファイルも含めた全てのファイルを一行ずつ表示することができます。 ( ちなみに開発をしていると `ls -la` はよく使います。)<br>

さぁここまできたら、久しぶりの Quiz を解いてみましょう。<br>
[quiz1.md](quiz1.md) へ Go です !
