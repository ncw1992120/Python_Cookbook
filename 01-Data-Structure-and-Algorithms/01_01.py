# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:我们有一个包含N个元素的元组或序列，现在想将他分解为N个单独的变量。
A:任何可迭代对象都可以通过一个简单的复制操作来分解为单独的变量。唯一的要求是变量的总数和结构要与序列相吻合。
"""
p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

#如果元素的数量不匹配，将得到一个错误提示。
p = (4, 5)
x, y, z = p
#Traceback (most recent call last):
#  File "<pyshell#10>", line 1, in <module>
#    x, y, z = p
#ValueError: need more than 2 values to unpack
