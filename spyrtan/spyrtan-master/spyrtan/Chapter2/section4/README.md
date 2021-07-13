# Git の使い方

前回 Unix Command というものを勉強しました。

### Git とは何か

みなさん GitHub というものを聞いたことがある or 使ったことがあるかもしれませんが、Git と GitHub は全くの別物です！<br>
今回は Git について勉強していきたいと思います。(GitHub についても後ほど勉強しますのでご安心を :rocket: )<br>
まずはこちらの、分かりやすくかかれた記事を読んでみてください。

https://www.sejuku.net/blog/5756

「4. Git を使う場面」まで読むと、 Git は

- バージョン管理ツールであること
- 分散型であること

がわかるかと思います。<br>


---

### なぜ Git を使うのか

Git を使う理由は

- バージョン管理ツールであること
- 分散型であること

です。

それぞれ詳しく紹介すると、

#### バージョン管理ツールであること

コードというのは、作品であり成果物です。<br>
つまり、だれがどの箇所をいつどのように変更したかといった情報が必要になります。（過去の自分は他人です）

こうした変更の情報を管理することができるのが Git です。<br>
また、「過去のこの点に戻したい！」といったことや、「この機能一旦外したい！」といったことが簡単に・正確にできます。

まとめると、共有資産であるコードを

- 責任の所在を明らかにすることができる
- 変更の情報を管理することができる

ものが Git です。

#### 分散型であること

これは、一見イメージしづらいですがとても重要です。<br>
逆に中央集権型のものをイメージするとわかりやすいので、Google Splead Sheet を例に考えていみましょう。

= 例

あなたは、業務効率化のためにシートAの配置を変更していました。<br>
ただ、今日は会議が多く、朝1時間ほど作業した後、17 時くらいにまたシートAを見に行きました。

するとせっかく整えていたシートAの配置がもとにもどっているではありませんか。<br>
あなたは、悲しさのあまり PC をそっと閉じ、退社しました。

=

さぁどうでしょう。これは、中央集権的にみんなで同じシートAを編集していたので、あなたの知らない間にだれかが書き換えてしまったのですね。<br>
一方で分散型の場合は、同じシートを編集せず手元にオリジナルのシートからコピーを取ってきて編集します。<br>
そして編集が終わったら、編集した内容をオリジナルのシートに反映させます。

つまり、編集している間、オリジナルのシートから切り離されるので知らない間にだれかが書き換えてしまうといったことがなくなります。<br>
この仕組みのおかげで、コードを複数人で開発することができるようになります。


#### まとめ

まとめです。<br>
今後みなさんのコードは部署内で広く使われるようになります。

その時に、

- どのような変更がされたかを管理する
- 誰がいつ変更したを管理する
- 複数人がコードを同時に触れるようにする

ことで、コードを管理する手間を削減するとともに、より安全で確実なものを作ることができるようになります。<br>
これがエンジニア以外でも組織全体で Git を使う価値です。

---

### Git のインストール

Git のうまみがなんとなく分かったところで早速導入していきましょう。<br>
Windows10 の場合はすでに Unix Command のセクションで済んでいるので、 macOS  のみ新しく導入していきます。<br>
Windows10 のみなさんは次の項目へどうぞ！

#### macOS に install 

まずは 

```shellscript
git --version
```

と terminal に入力してみてください。<br>

```shellscript
git version ...
```

というような表示が出た場合は Git がすでにインストールできています。<br>
上記のようにバージョン情報が出なかった場合は、

"Git" コマンドを実行するには、コマンドライン・デベロッパー・ツールが必要です。ツールを今すぐインストールしますか？

というポップアップが出るので、インストールをクリックしてインストールしてください。<br>
指示に従っていくとダウンロードできると思います。

再度

```shellscript
git --version
```

と入力し、バージョンが表示されれば正常にインストールできています。<br>
(インストール済みかどうか確認するときに、`Command --version` というようにオプションで version を指定する方法はよく使うので覚えておきましょう
)



---

### Git でバージョン管理してみよう


#### Git を利用する準備

さぁここからバージョン管理を体感していきましょう。<br>

1. Spyrtan 用のディレクトリを Desktop ディレクトリ配下に作成
2. Git を勉強するようのディレクトリを 1 で作成したディレクトリ配下に作成
3. Git を使用できるようにディレクトリを初期化

といったことをしていきます。<br>
まず、macOS であれば terminal を、windows であれば Git Bash を立ち上げましょう。

```shellscript
cd ~/Desktop
```

で Desktop ディレクトリに移動します。(コマンドの意味や言葉の意味が怪しい場合は適宜戻ってくださいね!)<br>
Desktop ディレクトリに Spyrtan 用のディレクトリを作成します。(名前はわかりやすく、`SPYRTAN__DIR`)にしています。

```shellscript
mkdir SPYRTAN__DIR
```

Spyrtan 用のディレクトリが作成できたら、`SPYRTAN__DIR` に移動しその中に `git_lesson` ディレクトリを作成しましょう。<br>
`git_lesson` ディレクトリを作成したら、`git_lesson` ディレクトリ内に移動してください。

カレントディレクトリを確認すると

```shellscript
(任意のパス)/Desktop/SPYRTAN__DIR/git_lesson
```

になっていればOKです。カレントディレクトリは `pwd` で確認できるんでしたね。<br>
ではこのディレクトリで Git を使えるようにしましょう。<br>
まずは、このディレクトリになんのファイルも入っていないことを `ls -la` で確認し、

```shellscript
git init
```

としましょう。こうすることで、Git が `git_lesson` ディレクトリ内で利用できるようになります。<br>
もう一度 `ls -la` とすると `.git` という隠しディレクトリが作成されていることがわかります。<br>
この `.git` ディレクトリがあるディレクトリでしか Git は使用することができないので注意しましょう！


最後に Git Command 全体の設定をしていきます。

```shellscript
git config --global user.name "motoya kondo"
git config --gloabl user.email "sample@mail.com"
```

というようにあなたの名前とメールアドレスを登録してください。<br>
これで Git をつかう準備は完成です。

#### 変更を保存する

Git における変更の保存は、２段階あります。<br>
分かりやすく引っ越しを例に出して説明しましょう。

| 段階 | Git のコマンド | 引っ越しでの説明 |
| -- | :--: | :--: |
| ステージングエリアに変更を保存する| `git add <file name>` | (食器用の)段ボールに詰めるものといらないものを仕分けする |
| コミットする | `git commit -m <commit message>` | 段ボールに必要な食器を詰めてガムテでぐるぐる巻きにし、段ボールの表面に「食器（割れ物注意）」と書く |

といった感じです。<br>
コードを書くときには、いろいろ試行錯誤すると思います。<br>
そこで、最初から変更を反映させるのではなくステージングエリアと呼ばれるところに変更を蓄積させていきます。(「ステージする」といいます)<br>
段ボールに詰める前に、なんとなく詰める予定のものを寄せておくのに似ていますね。

次に変更をコミットします。<br>
この時に、変更にたいしてメッセージを付けます。ちょうど仕分けをした食器を段ボールに詰め、ガムテで封をし、「食器（割れ物注意）」と書く感覚です。

このように、Git では変更の反映を２段階にわけることでストレスなく変更を保存することができます。<br>
早速 Git Command を利用していきましょう。

1. README.md の作成
2. README.md をステージ
3. README.md を修正
4. README.md をステージ
5. 変更をコミット
6. index.html を作成
7. index.html をステージ
8. 変更をコミット

の手順でやっていきます。

#### README.md の作成

READMEとは、まずはじめに読むマークダウンファイルになります。<br>
コードの使い方や、説明が書いてあるのが一般的です。

```shellscript
touch README.md
```

`touch` コマンドで作成できましたね。<br>

```shellscript
code .
```

として、VSCode を開きましょう。<br>
そして、`README.md` の内容を書いていきます。

```markdown
# README
```

このようにファイルを作成しました<br>
ここで、`git status` というコマンドで現在の状況を確認してみましょう。

```shellscript
git status

On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

のように表示されているかと思います。<br>
Untracked files のところに `README.md` が追加されているのが分かるかと思います。<br>
つまり、「ディレクトリの中にあるけど、Git にまだ認識されていないファイルだよ」ということです。

#### README.md をステージ

`git add <file name>` とすればステージングエリアに変更をステージできます。

```shellscript
git add README.md
```

`git status` で状況を確認してみましょう

```shellscript
git status

On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

このように `README.md` が Change to be commited に追加されていますね。<br>
「やっぱステージングエリアから外したい」というときには `git reset <file name>` とすればOKです。

```shellscript
git reset README.md
```

`git status` で状況を確認すると、change to be commited から外されているのが確認できるかと思います。<br>
再び `git add` でファイルを追加しておきましょう。

#### README.md を修正 / README.md をステージ

少し README を修正して、変更をステージしてみましょう。

```markdown
# README

## what is it
```

このように修正して保存しました。<br>
この状況で `git status` を見ると

```shellscript
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
```

このように修正されたファイルがあることが分かります。<br>
ちなみに、ファイルの差分は `git diff` とするとみることができます。<br>

```shellscript
git diff

diff --git a/README.md b/README.md
index 52da238..57e0ec2 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,3 @@
-# README
\ No newline at end of file
+# README^M
+^M
+## What is it
\ No newline at end of file
```

実はこれは VSCode で分かりやすく＆詳しく見れるので、そちらがおすすめです。<br>
では変更をステージしましょう。`git add` ですね。

変更を反映できたら `git status` で状況を確認してみましょう。

#### 変更をコミット

次に変更をコミットしていきます。<br>
ステージングエリアにある変更がコミットされるのでしたね。<br>
(`git status` で change to be committed にある変更がコミットされます)

コミットは引っ越しの段ボール詰めと一緒で、ある程度まとまった単位でします。<br>
(風呂用品と食器を一緒にしたら大変ですね)

では今回は `README.md` を追加したので

```shellscript
git commit -m "README.md の作成"
```

としましょう。

```shellscript
git status
```

とするとステージングエリアから変更がなくなっていることが確認できます。<br>
`git log` とするとあなたのコミットが確認できるはずです。

```shellscript
git log

commit cf150ddb17e82ad0986d81f0c02970032b642b87 (HEAD -> master)
Author: motoyannn <techvo.1127@gmail.com>
Date:   Thu Sep 17 00:48:34 2020 +0900

    README.md の作成
```

こんな感じですね。<br>
ちなみに `git show <commit hash>` とすることで変更の内容を確認することができます。

####  index.html を作成 / index.html をステージ / 変更をコミット

さて最後に index.html を作成し、ステージ、コミットまでしてみましょう。<br>
ここまでできればばっちりです。

最後に、[quiz2.md](quiz2.md) を解いて到達具合を確認していきましょう。
