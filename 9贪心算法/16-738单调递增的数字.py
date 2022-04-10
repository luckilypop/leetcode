#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/10 14:48
# @Author  : yq
# @File    : 16-738单调递增的数字.py
# @Software: PyCharm

'''

def monotoneIncreasingDigits(n):
    a = list(str(n))
    for i in range(len(a)-1, 0, -1):
        if int(a[i]) < int(a[i-1]):
            a[i-1] = str(int(a[i-1])-1)
            a[i:] = '9' * (len(a)-i)
    return int("".join(a))

print(monotoneIncreasingDigits(3322))