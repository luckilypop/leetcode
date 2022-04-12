#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/12 8:48
# @Author  : yq
# @File    : 6-343整数拆分.py
# @Software: PyCharm

'''


def integerBreak(n):
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        for j in range(1, i-1):
            dp[i] = max(dp[i],max(j * (i-j), j* dp[i-j]))
    return dp[n]

print(integerBreak(5))