# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:在字典上对数据执行各式各样的计算(比如求最小值、最大值、排序等)。
A:为了对字典值做计算，通常会利用zip()将字典的键和值反转过来。
"""
prices = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HPQ': 37.20,
	'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))
