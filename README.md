# アルゴリズム実装チャレンジ

`MaxWordCounter.py` は、与えられた英文の中で最も頻繁に出現する単語を検出する、Pythonプログラムです。<br>
制限時間30分以内に、この問題に対する効率的なアルゴリズムを設計・実装してください。

## セットアップ

1. 対象のリポジトリをクローンしてください。

```bash
git clone https://github.com/yuijiro473/algorithm-challenge 
```

2. 以下の規則に従い、ブランチを作成してください。

   ブランチ名：`{gitユーザー名}-challenge`

## 問題

与えられた文章中に出現する単語の頻度をカウントし、最も頻度の高い単語を返す関数を作成してください。<br>
対象の`MaxWordCounter.py`に詳しい記載があります。<br>

## 解答方法
下記の関数に問題文の条件を満たすコードを記載してください。

```python
def most_frequent_word(text):
    # ここにコードを書いてください
    pass
```

## テスト

既存の`test_most_frequent_word()` 関数を呼び出すことで、作成した関数のテストを実行できます。

```python
def test_most_frequent_word():
    assert most_frequent_word("the quick brown fox jumps over the lazy dog") == "the"
    assert most_frequent_word("hello world world world") == "world"
    assert most_frequent_word("a") == "a"
    assert most_frequent_word("this is a longer text with several words but only one word is repeated repeated") == "repeated"
    assert most_frequent_word("repeated repeated repeated") == "repeated"
    assert most_frequent_word("word") == "word"
    assert most_frequent_word("several words but none are repeated") in ["several", "words", "but", "none", "are", "repeated"]
    assert most_frequent_word("this this this that that") in ["this", "that"]
    print("課題クリア")

test_most_frequent_word()
```

## 注意点

- 文章は英語とし、すべての単語は小文字で、句読点や特殊文字は含まれていません。
- 標準ライブラリの使用：可
- 最も頻度の高い単語が複数存在する場合は、そのうちの任意の1つを返して構いません。

## クリア条件

『最も頻度の高い単語を返す』という条件を満たし、ターミナルに「課題クリア」の表示が出ればチャレンジクリアです。

## 勝利条件

- 一方がチャレンジ成功：成功者の勝利
- 両者チャレンジ成功orチャレンジ失敗：引き分け

## 提出
チャレンジ終了後、修正したファイルを作成したブランチにプッシュしてください。
