#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/10 15:04
# @Author  : yq
# @File    : 17-714买卖股票的最佳时机含手续费.py
# @Software: PyCharm

'''


def maxProfit(prices,fee):
    res = 0
    minP = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < minP:
            minP = prices[i]
        elif prices[i] > minP and prices[i] <= minP + fee:
            continue
        else:
            res += prices[i] -minP + fee
            minP = prices[i] -fee
    return res