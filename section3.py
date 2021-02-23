#!/usr/bin/env python
# coding: utf-8

# # 【第3回】BeautifulSoupの使い方①
# 
# 
# 前回のレクチャーでは、PythonからURLにアクセスするためのライブラリ`Requests`について学習しました。
# 
# `Requests`を使うことで、対象のURLからHTML自体は取得できました。
# 
# でも、自分が本当に欲しいテキスト情報については、まだ取得できていない状況です。
# 
# <br>
# 
# 最終的な目標にしている「テキストデータの取得」には、**`Requests`で取得したHTMLを、`BeautifulSoup`で解析する必要があります。**
# 
# というわけで、今回は取得したHTMLを解析するために、`BeautifulSoup`の使い方を習得していきましょう。
# 
# *※動画の感想を、僕のTwitterにメンションしてツイートしていただけると嬉しいです（ ;  ; ）！*
# 
# Twitter : [@hayatasuuu](https://twitter.com/hayatasuuu)
# 
# ## BeautifulSoupとは？
# 
# `BeautifulSoup`とは、HTMLを解析するためのライブラリです。
# 
# [»公式ページ :Beautiful Soup Documentation — Beautiful Soup 4.9.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# 
# <br>
# 
# BeautifulSoupを使ってHTMLを解析することで、自分が欲しい値を取得しやすいします。
# 
# 例えば、以下のフルーツリストから、フルーツの名前を取得する場合を考えてみましょう。
# 
# <ol>
#     <li>りんご</li>
#     <li>バナナ</li>
#     <li>もも</li>
# </ol>
# 
# こういった場合に、**BeautifulSoupを使えば「`<li>`タグに入っている情報を取得する」**といった使い方ができます。
# 
# *※逆に、BeautifulSoupを使わずにフルーツを取得しようとすると「正規表現を使って`<li></li>`の中身を取り出す」といった感じになって、複雑なコードを書く必要があります。*
# 
# <br>
# 
# いまはリストが1つしかありませんが、通常のWebページであればリストが複数出てきてもおかしくありません。
# 
# <ol>
#     <li>りんご</li>
#     <li>バナナ</li>
#     <li>もも</li>
# </ol>
# 
# <ol>
#     <li>なし</li>
#     <li>ぶどう</li>
#     <li>いちご</li>
# </ol>
# 
# このような場合に、「ももだけ取り出したい...」と思ったら、正規表現で取得するのは非常に大変です。
# 
# なので、原理原則は「**Requestsで取得したデータは、BeautifulSoupでHTMLを解析する**」とことを覚えておきましょう！

# # 取得したHTMLを、BeautifulSoupで解析する
# 
# スクレイピングの流れをもう一度おさらいしておくと、以下のようになっていました。
# 
# 1. RequestsでHTMLを取得する
# 2. 取得したHTMLを解析する(BeautifulSoup)
# 3. 自分が欲しい情報を取得する
# 
# 「①RequestsでHTMLを取得する」については前回のレクチャーで学習していますので、今回はそれ以降の②と③をやっていきたいと思います。

# ## 必要なライブラリのインポート
# 
# まずは今回使うライブラリをインポートしていきましょう。
# 
# 必要になるライブラリは、前回も紹介した`Requests`と`BeautifulSoup`です。
# 
# <br>
# 
# 新しく仮想環境を作成している場合には、以下のコマンドでライブラリのインストールをしましょう。
# 
# *※実行するときは、コメントアウト(`#`)を外してください！*

# In[ ]:


## Anacondaを利用している方
# ! conda install beautifulsoup4 -y


# In[1]:


import requests
from bs4 import BeautifulSoup


# これで今回使うライブラリの準備が完了しました。
# 
# まずは前回同様に、WebページからHTMLを取得していきましょう。

# ## RequestsでHTMLを取得する
# 
# 前回と同じで、Pythonの公式ページからHTML情報を取得していきたいと思います。
# 
# https://www.python.org/
# 
# 上記のURLに対して、Requestsを使ってアクセスしてみましょう。

# In[2]:


# 変数urlに、Python公式ページのURLを入れる
url = "https://www.python.org/"
# URLにアクセスした結果を、変数rに代入する
r = requests.get(url)


# これでPython公式ページへのアクセスが完了しました。
# 
# レスポンス結果からHTMLを取得するには、以下のように書きましたね。

# In[3]:


# Python公式ページのHTMLを表示
print(r.text)


# ちなみに、取得結果の型を確認してみると、これは単なる文字列になっています。

# In[4]:


# 取得したテキストの型を確認する
type(r.text)


# BeautifulSoupでHTMLを解析するときは、文字列を対象にします。
# 
# なので、`Requests`で取得してきたHTMLは、そのままBeautifulSoupに投入して大丈夫です。
# 
# <br>
# 
# と、あれこれ言われてもよく分からない部分があると思うので、さっさとBeautifulSoupを使ってみましょう！笑

# ## 取得したHTMLを解析する
# 
# 結論、取得してきたHTMLを解析するには、以下のように書いてあげます。

# In[5]:


# BeautifulSoupでHTMLを解析する
soup = BeautifulSoup(r.text)


# この1行だけで、単なる文字列だったリクエスト結果から、あとはタグを指定するだけで欲しいデータを取得できるようになります。
# 
# *※変数名の`soup`ですが、慣習的にBeautifulSoupの解析結果を、こう名付けることが多いです。*
# 
# <br>
# 
# あとは、ここから自分が欲しいデータを取得するだけです！

# ## 自分が欲しい情報を取得する
# 
# 今回はPythonの公式ページから、`<h2>`タグに書かれている内容を取得したいと思います。
# 
# [Python公式ページ](https://www.python.org/)をデベロッパーツール(検証)で見るとわかりますが、`<h2>`タグは色々なところで使われています。
# 
# <br>
# 
# これらの`<h2>`タグから、まずは最初の1つである`Get Started`だけ取得していきましょう。
# 
# `soup`から`<h2>`の情報を抽出するには、以下のように記述します。

# In[7]:


# soupから最初のh2を取得する
soup.h2


# 上記のように書いてあげると、最初にヒットする`<h2>`をタグごと取得できます。
# 
# また、`soup.h2`以外にも、以下のような書き方が可能です。

# In[15]:


# soupから最初のh2を取得する(soup.h2以外で)
soup.find('h2')


# どちらの方法でも、`<h2>`タグの情報を取得できているかと思います。
# 
# ここから中身のテキストを取得するのも非常にカンタンで、以下のように書いてあげるだけです。

# In[17]:


# soup.h2の方法でテキストを取得する
soup.h2.text
# soup.find('h2')の方法でテキストを取得する
soup.find('h2').text


# どちらの方法でも、同じように「Get Started」を取得できました。
# 
# また、テキストを取得する方法も2つあり、以下のように書くこともできます。

# In[13]:


# soup.h2の方法でテキストを取得する
soup.h2.get_text()
# soup.find('h2')の方法でテキストを取得する


# ここまで聞くと、なんだかややこしくなってきますよね。
# 
# なので「自分はこの方法で取得するんだ！」という方法を決めておくのがオススメです。
# 
# <br>
# 
# 参考程度に、僕がいつも使っている方法は、以下のようになっています。
# 
# - タグを取得するとき : `soup.find()`
# - テキストを取得するとき : `soup.find().text`
# 
# タグの取得の関しては、このあと紹介しますが複数の`<h2>`タグを取得するとき`find_all()`を使います。
# 
# `find()`と`find_all()`のセットで使ってあげると分かりやすいので、1つのタグを取得するときは`find_all()`がオススメです。
# 
# <br>
# 
# また、`get_text()`ではなく`text`を使っているのは、1つに「簡潔に書ける」という意味があります。
# 
# 他には、Pythonの辞書からvalueを取得するとき、該当しないKeyで`get()`を使うとNoneが返ってくるのに対し、`get_text()`ではエラーを返します。
# 
# 自分の中で`get()`はNoneを返すという頭になっているので、BeautifulSoupでテキストを取得するときは`.text`を使うようにしています。
# 
# <br>
# 
# とは言っても、人によって好みがあると思うので、お好きな方法で要素から情報を取得してみてください(｀・ω・´)！
# 
# この講義シリーズでは、自分がいつも使っている以下の方法で進めさせてくださいm(_ _)m
# 
# - タグを取得するとき : `soup.find()`
# - テキストを取得するとき : `soup.find().text`

# # 演習
# 
# [テックダイアリー(僕のブログ)](https://tech-diary.net)の以下の記事で、ブログタイトルを「文字列で」取得してみましょう。
# 
# https://tech-diary.net/python-scraping-books/
# 
# <br>
# 
# *※できれば1回のリクエストで情報取得していただけると嬉しいです（ ;  ; ）*

# In[18]:


url = 'https://tech-diary.net/python-scraping-books/'
r = requests.get(url)


# In[19]:


print(r.text)


# In[20]:


type(r.text)


# In[21]:


soup = BeautifulSoup(r.text)


# In[22]:


soup.find("h1")


# In[23]:


soup.find("h1").text


# In[24]:


soup.find("h2")


# In[25]:


soup.find("h2").text


# In[26]:


url = 'https://www.starbucks.co.jp/'
r = requests.get(url)


# In[27]:


print(r.text)


# In[28]:


soup = BeautifulSoup(r.text)


# In[29]:


type(r.text)


# In[31]:


soup.find("h1")


# In[32]:


soup.find("h1").text


# In[33]:


soup.find("h2")


# In[34]:


soup.find("h3")


# In[35]:


soup.find("p")


# In[37]:


soup.find("title")


# In[38]:


soup.find("title").text


# In[ ]:




