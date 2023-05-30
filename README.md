# MaxWordCounter

`MaxWordCounter` は、与えられた英文の中で最も頻繁に出現する単語を検出する Python プログラムです。制限時間30分以内に、この問題に対する効率的なアルゴリズムを設計・実装することが目標です。

## 問題

与えられた文章中に出現する単語の頻度をカウントし、最も頻度の高い単語を返す関数を作成してください。文章は英語とし、すべての単語は小文字で、句読点や特殊文字は含まれていません。

以下にスケルトンコードを提供します。この関数を完成させてください。

```python
def most_frequent_word(text):
    # ここにコードを書いてください
    pass
```

## 注意点

- 最も頻度の高い単語が複数存在する場合は、そのうちの任意の1つを返して構いません。

## テスト

既存の`test_most_frequent_word()` 関数を呼び出すことで、作成した関数のテストを実行できます。

```python
def test_most_frequent_word():
    assert most_frequent_word("the quick brown fox jumps over the lazy dog") == "the"
    assert most_frequent_word("hello world world world") == "world"
    assert most_frequent_word("a") == "a"
    print("課題クリア")

test_most_frequent_word()
```

すべてのテストをパスし、ターミナルに「課題クリア」の表示が出ればチャレンジクリアです。