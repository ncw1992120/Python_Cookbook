#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#Q:我们的代码是通过位置来访问列表或元祖的，但有时这会使代码变得有些难以阅读。
#  我们希望可以通过名称来访问元素，以此减少结构中对位置的依赖性。
#A:相比普通的元祖，collections.namedtuple()只增加了极小的开销就提供了这些便利。
#  实际上这是一个工厂方法，它返回的是Python中标准元祖类型的子类。
#  我们提供给它一个类型名称以及相应的字段，它就返回一个可实例化的类，为你已经定义好的字段传入值等。
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-03-05 18:03:52
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub, sub.addr, sub.joined)
#namedtuple是字典的一种替代，如果构建涉及字典的大型数据结构，namedtuple更加高效
#与字典不同的是，namedtuple是不可变的。可以用_replace()方法来修改属性
sub = sub._replace(joined='2016-02-28')
print('Replaced:',sub)


Stock = namedtuple('Stock', ['name','shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

