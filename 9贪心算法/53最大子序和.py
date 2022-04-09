#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/8 13:49
# @Author  : yq
# @File    : 53最大子序和.py
# @Software: PyCharm

'''
def maxSubArray(nums):
    res = -float('inf')
    count = 0
    for i in range(len(nums)):
        count += nums[i]
        if count > res:
            res = count
        # 需要考虑到此点
        if count < 0:
            count = 0
    return res

