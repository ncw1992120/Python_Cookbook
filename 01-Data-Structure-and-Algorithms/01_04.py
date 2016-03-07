# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:在某个集合中找出最大火最小的N个元素。
A1:在所找的元素数量较少时可以使用heapq模块中的两个函数nlargest()和nsmallest()
A2:如果和集合中元素的总数目相比N非常小，则可以使用heapq的heapify()函数，heapify()函数只可对列表使用
A3:如果只是简单地想找到最小或最大的元素(N=1时)，那么用min()和max()会更加快。
A4:如果N和集合本身的大小差不多大，通常更快地方法是先对集合排序，然后做切片操作。例如：sorted(items)[:N]
"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

#这两个函数都可以接受一个参数key,从而允许它们工作在更复杂的数据结构之上。

portfolio = [
	{'name': 'IBM', 'shares': '100', 'price': 91.1},
	{'name': 'AAPL', 'shares': '50', 'price': 543.22},
	{'name': 'FB', 'shares': '200', 'price': 21.09},
	{'name': 'HPQ', 'shares': '35', 'price': 31.75},
	{'name': 'YHOO', 'shares': '45', 'price': 16.35},
	{'name': 'ACME', 'shares': '75', 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])
print(cheap)
print(expensive)

heap = list(nums)
heapq.heapify(heap)
print(heap)

heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
