#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/28 10:11
# @Author  : yq
# @File    : 202快乐数.py
# @Software: PyCharm

'''
# 编写一个算法来判断一个数 n 是不是快乐数。
#
#  「快乐数」 定义为：
#
#
#  对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
#  然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
#  如果这个过程 结果为 1，那么这个数就是快乐数。
#
#
#  如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
#
class Solution:
    def isHappy(self, n):
        def calculate_sum(num):
            sum = 0
            while num:
                sum += (num % 10) ** 2
                num = num // 10
            return sum
        record = set()

        while True:
            n = calculate_sum(n)
            if n == 1:
                return True
            if n in record:

                return False
            else:
                record.add(n)
if __name__ == '__main__':
    a = Solution()
    b = 19
    temp = a.isHappy(b)
    print(temp)
