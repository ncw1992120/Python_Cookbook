# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:我们的代码已经变得无法阅读，到处都是硬编码的切片索引，我们想将它们清理干净。
"""
#假设有一些代码用来从字符串的固定位置中取出具体的数据
record = '13215946513248795321698792 13216574987 21321657987 3151654 98436132.54 465165798'
cost = int(record[20:32]) * float(record[40:48])
#可以对切片命名，以避免许多神秘难懂的硬编码索引
SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
