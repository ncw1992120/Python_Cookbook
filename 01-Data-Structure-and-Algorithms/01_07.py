# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:创建一个字典，同时当对字典做迭代或序列化操作时，也能控制其中元素的顺序。
A:可以使用collections模块中的OrderedDict类，当对字典做迭代时，他会严格按照元素初始添加的顺序进行
"""
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d: print(key, d[key])
