#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/23 9:18
# @Author  : yq
# @File    : 69x的平方.py
# @Software: PyCharm

'''

# 题目
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#  由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

# 说明：二分之二分
class Solution:
    def mySqrt(self, x):
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid < x/mid: # 防止mid * mid 溢出
                left = mid + 1
            elif mid > x/mid:
                right = mid - 1
            else:
                return mid
        return right

