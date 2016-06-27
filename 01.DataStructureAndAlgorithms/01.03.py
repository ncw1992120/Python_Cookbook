# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:我们希望在迭代或是其他形式的处理过程中对最后几项纪录做一个有限的历史记录统计。
A:使用collections.deque保存有限的历史记录。
"""
#对一系列文本行做简单的文本匹配操作，当发现有匹配时就输出当前的匹配行以及最后检查过的N行文本。
from collections import deque

def search(lines, pattern, history):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

if __name__ == '__main__':
	with open('3.txt') as f:
		for line, prevlines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
				print(line,end='')
				print('-'*20)
