#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/11 10:10
# @Author  : yq
# @File    : 2-70爬楼梯.py
# @Software: PyCharm

'''


def climbStairs(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1
    for i in range(2, n + 1):
        d[i] = d[i - 2] + d[i - 1]
    return d[n]
