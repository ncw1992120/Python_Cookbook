#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#Q:我们需要调用一个换算(reduction)函数(例如sum()、min()、max())，但首先得对数据做转换或筛选
#A:在函数参数中使用生成器表达式可以非常优雅地解决这个问题
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-27 17:28:13

#如果想计算平方和，可以象下面这样做
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

#确定一个目录下是否存在python文件
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python')

#将元组转换为CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

#数据结构转换
portfolio = [
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL', 'shares':20},
    {'name':'SCOX', 'shares':65},
  ]
  min_shares = min(s['shares'] for s in portfolio)
