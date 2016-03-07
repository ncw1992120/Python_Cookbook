# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Q:需要从某个可迭代对象中分解出N个元素，但是这个可迭代对象的长度可能超过N，这会导致出现"分解的值过多(too many values to unpack)"的异常。
A:Python的"*表达式"可以用来解决这个问题
"""
#假设有一些用户记录，记录由姓名和电子邮件地址组成，后面跟着任意数量的电话号码。
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name, email, phone_numbers)

#假设有一门课程，在期末的作业成绩中去掉第一个和最后一个，只对中间剩下的成绩作平均分统计。
grades = [85, 87, 88, 92, 96, 99]
first, *middle, last = grades
print(first, middle, last)

#用一系列的值来代表公司过去8个季度的销售额。如果想对最近一个季度的销售额同前7个季度的平均值做比较。
sales_record = [55, 58, 68, 48, 57, 53, 69, 60]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg, current_qtr)
