def most_frequent_word(text):
    # ここにコードを書いてください
    pass


def test_most_frequent_word():
    assert most_frequent_word("the quick brown fox jumps over the lazy dog") == "the"
    assert most_frequent_word("hello world world world") == "world"
    assert most_frequent_word("a") == "a"
    assert most_frequent_word("repeated repeated repeated") == "repeated"
    assert most_frequent_word("word") == "word"
    assert most_frequent_word("several words but none are repeated") in ["several", "words", "but", "none", "are", "repeated"]
    assert most_frequent_word("this this this that that") in ["this", "that"]
    print("課題クリア")

test_most_frequent_word()