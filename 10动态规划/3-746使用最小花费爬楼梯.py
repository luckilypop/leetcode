#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/11 10:21
# @Author  : yq
# @File    : 3-746使用最小花费爬楼梯.py
# @Software: PyCharm

'''


def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return min(dp[n-1],dp[n-2])
