#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/8 13:54
# @Author  : yq
# @File    : 4-122买卖股票的最佳时机II.py
# @Software: PyCharm

'''
def maxProfit(prices):
    # 自己思路，保存正数
    res = []
    for i in range(len(prices)-1):
        temp = prices[i+1] - prices[i]
        if temp > 0 :
            res.append(temp)
    count = 0
    for i in range(len(res)):
        count += res[i]
    return count

def maxProfit2(prices):
    res = 0
    for i in range(len(prices)-1):
        res += max((prices[i+1] - prices[i]), 0)
    return res
