# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:序列中含有一些数据，我们需要提取出其中的值或根据某些标准对序列做删减。
A:要筛选序列中的数据，通常最简单的方法是使用列表推导式(list comprehension)。
"""
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

[n for n in mylist if n > 0]
[n for n in mylist if n < 0]

#如果原始输入非常大，可以考虑使用生成器表达式通过迭代的方法产生筛选的结果。
pos = (n for n in mylist if n > 0)
for x in pos:
	print(x)

#如果筛选的标准没法简单地表示在列表推导式或生成器表达式中，可以将处理筛选逻辑的代码放到单独的函数中，然后使用内建的filter()函数处理
values = ['1', '2','-3', '-', '4', 'N/A', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))

print(ivals)

#筛选工具itertools.compress()可以接受一个可迭代对象以及一个布尔选择器序列作为输入。
#输出时，它会给出所有在相应的布尔选择器中为True的可迭代对象元素。
#如果想把对一个序列的筛选结果施加到另一个相关的序列上时，这就会非常有用。
addresses = [
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH',
	'2122 N CLARK',
	'5645 N RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BROADWAY',
	'1039 W GRANVILLE'
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
