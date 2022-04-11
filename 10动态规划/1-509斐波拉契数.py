#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/11 10:02
# @Author  : yq
# @File    : 1-509斐波拉契数.py
# @Software: PyCharm

'''
def fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(1,n):
        c = a + b
        a, b = b, c
    return c