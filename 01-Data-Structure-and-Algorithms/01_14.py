# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:在同一个类的实例之间做排序，但是它们并不原生支持比较操作。
A:内建的sorted()函数可接受一个用来传递可调用对象(callable)的参数key，而该可调用对象会返回待排序对象中的某些值，sorted则利用这些值来比较对象。
"""

class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print(users)
print(sorted(users, key=lambda u: u.user_id))

#除了可以用lambda表达式外，另一种方式是使用operator.attrgetter()。
#operator.attrgetter()函数会更快一些，并且具有允许同时提取多个字段值的能力。
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))
