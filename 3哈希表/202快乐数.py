#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/28 10:11
# @Author  : yq
# @File    : 202快乐数.py
# @Software: PyCharm

'''
class Solution:
    def isHappy(self, n):
        def calculate_sum(num):
            sum = 0
            while num:
                sum += (num % 10) ** 2
                num = num // 10
            return sum
        record = set()
        print(record,type(record))
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
