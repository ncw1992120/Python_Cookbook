#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#Q:我们想创建一个字典，其本身是另一个字典的子集
#A:利用字典推导式可轻松解决
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-03-05 17:49:10

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75}

p1 = { key:value for key, value in prices.items() if value > 200}
print(p1)

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = { key:value for key, value in prices.items() if key in tech_names}
print(p2)

#大部分可利用字典推导式解决的问题也可以通过创建元祖序列然后将它们传给dict()函数来完成
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
#但是字典推导式的方案更加清晰，而且也快得多(本例中的字典效率要高2倍多)

#有时会用多种方法完成同一件事
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = { key:prices[key] for key in prices.keys() & tech_names }
print(p2)
#但是这种解决方案比第一种要慢1.6倍
