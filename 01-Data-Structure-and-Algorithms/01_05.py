# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:实现一个队列，他能够以给定的优先级来对元素排序，且每次pop操作时都会返回优先级最高的那个元素。
A:下面利用heapq模块实现了一个简单的优先级队列
"""
import heapq

class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0
	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1
	def pop(self):
		return heapq.heappop(self._queue)[-1]

class Item:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
