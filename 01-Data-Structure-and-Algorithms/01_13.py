# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:有一个字典列表，项根据一个或多个字典中的值来对列表排序。
A:可以利用operator模块中的itemgetter函数对这类结构进行排序。本节中的技术同样适用于min()和max()。
"""

#假设通过查询数据库表项获取网站上的成员列表，我们得到了如下的数据结构：
rows = [
	{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
	{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
	{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname': 'Big', 'lname': 'Jones', 'uid': 1000}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

#itemgetter()函数还可以接受多个键。例如：
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

print(rows_by_lfname)

#有时会用lambda表达式来取代itemgetter()的功能，这种解决方案通常也能正常工作。但是用itemgetter()通常会运行的更快一些。
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=lambda r: r['uid'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
