#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/9 10:47
# @Author  : yq
# @File    : 8-134加油站.py
# @Software: PyCharm

'''

def canCompleteCircuit(gas, cost):
    start = 0
    curSum = 0
    totalSum = 0
    for i in range(len(gas)):
        res = gas[i] - cost[i]
        curSum += res
        totalSum += res
        if curSum < 0:
            curSum = 0
            start = i + 1
    if totalSum < 0:
        return -1
    return start

