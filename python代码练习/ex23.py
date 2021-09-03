# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/20  15:29

#break_words：使用split方法把一个句子字符串分隔个单个得单词放入列表
def break_words(stuff):
    """This function will break up words for us."""
    words=stuff.split(' ')
    return words

#排序
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#print_first_word：使用pop(0)方法弹出列表中第一个元素
def print_first_word(words):
    """Prints the first word after popping it off."""
    word=words.pop(0)
    print(word)

#print_last_word：使用pop(-1)方法弹出列表最后一个元素
def print_last_word(words):
    """Prints the last word after popping it off"""
    word=words.pop(-1)
    print(word)

#sort_sentence：结合break_words和sort_words
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words=break_words(sentence)
    return sort_words(words)

#print_first_and_last：调用break_words和print_first_word、print_last_word
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#print_first_and_last_sorted：调用sort_sentence和print_first_word、print_last_word
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)