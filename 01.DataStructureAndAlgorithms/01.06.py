# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:做一个能将键映射到多个值的字典。
A:字典是一种关联容器，每个键都映射到一个单独的值上。如果想让键映射到多个值，需要将这多个值保存到另一个容器如列表或集合中。
"""
d = {
	'a': [1,2,3],
	'b': [4,5]
}

e = {
	'a': {1,2,3},
	'b': {4,5}
}

#为了能更方便地创建这样的字典，可以使用collections模块中的defaultdict类。
#defaultdict的一个特点就是它会自动初始化第一个值，这样只需关注添加元素即可。
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
d['b'].add(4)
d['b'].add(5)
