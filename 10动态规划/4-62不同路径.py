#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/11 10:31
# @Author  : yq
# @File    : 4-62不同路径.py
# @Software: PyCharm

'''
# m行n列
# dp = [[0 for j in range(column)] for i in range(row)]
def uniquePaths(m, n):
    dp = [[1 for j in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
