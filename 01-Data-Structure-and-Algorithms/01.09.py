# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:有两个字典，找出它们中间可能相同的地方。
A:要找出两个字典的相同之处，只需通过keys()或者items()方法执行常见的集合操作即可。
"""
a = {
	'x' : 1,
	'y' : 2,
	'z' : 3
}

b = {
	'w' : 10,
	'x' : 11,
	'y' : 2
}

#Find keys in common
a.keys() & b.keys()

#Find keys in a that are not in b
a.keys() - b.keys()

#Find (key,value) pairs in common
a.items() & b.items()

#这些类型的操作也可用来修改或过滤掉字典中的内容。
#Make a new dictionary with centain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
