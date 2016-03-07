# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:去除序列中出现的重复元素，但仍然保持剩下的元素顺序不变。
"""
#如果序列中的值是可哈希的，那么这个问题可以通过使用集合和生成器轻松解决。
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

#如果序列不可哈希，则可以指定一个函数用来将序列中的元素转换为可哈希的类型，这么做的目的是为了检测重复项
def dedupe(items, key = None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))
