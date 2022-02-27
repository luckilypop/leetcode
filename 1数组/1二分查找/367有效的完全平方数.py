#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/23 9:30
# @Author  : yq
# @File    : 367有效的完全平方数.py
# @Software: PyCharm

'''

# 题目
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，
# 则返回 true ，否则返回 false 。

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right ) // 2
            if mid == num/mid:
                return True
            elif mid < num/mid:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == '__main__':
    a = Solution()
    temp = a.isPerfectSquare(16)
    print("temp:",temp)