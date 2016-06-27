# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:有一个元素序列，想知道在序列中出现次数最多的元素是什么。
A:collections模块中的Counter类正是为此类问题所设计的。
"""
from collections import Counter

words = "look into my eyes look into my eyes the eyes the eyes the eyes not around the eyes don't look around the eyes look into my eyes you're under"
words = words.split()
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

#如果想要增加计数，只需简单地自增即可
morewords = "why are you not looking in my eyes"
morewords = morewords.split()
word_counts.update(morewords)
top_three = word_counts.most_common(3)
print(top_three)

#Counter对象还可以轻松的同各种数学运算操作结合起来使用
a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b
print(c)
print(d)
