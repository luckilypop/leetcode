#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/9 10:29
# @Author  : yq
# @File    : 7-1005K次取反后最大化的数组和.py
# @Software: PyCharm

'''
def largestSumAfterKNegations(A, k):
    # 第一步：将A按绝对值从大到小排列
    A = sorted(A, key=abs, reverse=True)
    # 第二步：从前向后遍历，遇到负数将其变为正数，同时K--
    for i in range(len(A)):
        if A[i] < 0 and K > 0:
            A[i] = abs(A[i])
            k -= 1
    # 第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
    if k % 2 == 1:
        A[len(A)-1] *= -1
    # if K > 0:
    #             A[-1] *= (-1)**K #取A最后一个数只需要写-1
    # 第四步：求和 return sum(A)
    res = 0
    for i in range(len(A)):
        res += A[i]
    return res
