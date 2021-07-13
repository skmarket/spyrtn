
def quiz1():
    """
    [問題１]

    100 以上 1000 以下の数のうち 
    13 の倍数時には、'fizz'
    31 の倍数時には、'buzz'
    13 の倍数かつ 31 の倍数のときには 'fizzbuzz'
    それ以外の時には、数値をそのまま

    `print()` を利用して表示してください。

    出力例

    ```output
    100
    (略)
    115
    116
    'fizz'
    118
    (略)
    1000
    ```
    """
    pass


def quiz2(a=0, b=1):
    """
    [問題２]

    じゃんけんを a さん、ｂさんがします。
    グー：0
    チョキ：1
    パー:2
    という入力値で、関数の引数として渡されます。
    
    a さんが勝つ場合には、'win' 
    あいこの時は 'draw' 
    負けたときは 'lose'

    と返してください。(関数の返り値に指定するということです)

    quiz2 関数のキーワード引数は自由に変更して、
    quiz2() を実行することで debug してみてください

    debug
    https://wa3.i-3-i.info/word1419.html
    """
    pass


def quiz3(a=1, b=1, c=1):
    """
    [問題３]

    じゃんけんを a さん、ｂさん c さんがします。
    グー：0
    チョキ：1
    パー:2
    という入力値で、関数の引数として渡されます。
    
    a さんが勝つ場合には、'win' 
    あいこの時は 'draw' 
    負けたときは 'lose'

    と返してください。
    """
    pass



"""
[問題４]

Web サイトにビーコン https://www.torimochi.jp/706/ をしこんだので、
どれくらいの人がそのサイトに訪問したかが分かります。
この値を num_viewer に格納します

また、そのサイトが開かれている時間を time_viewer　に格納しています。

これら２つの値を引数として受け取り、1人あたりの訪問時間を返す関数を作成してください。
ただし関数名は、time_per_person とします
"""

def time_per_person(num_viewer, time_viewer):
    pass




"""
[問題４]

あるサイトについて、 time_per_person で求めた平均よりも
閲覧時間が長い場合には、通知する関数 notification() を invoke したいです。

それぞれの施策を打っているサイトでの滞在時間 staying_time を仮引数と
して受け取り、平均滞在時間以上の場合　notification() を invoke する関数
check_time 関数を実装してください
"""

def notification():
    print('長く見られたよ！')

def check_time():
    pass
