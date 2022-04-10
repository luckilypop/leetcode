#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/8 14:14
# @Author  : yq
# @File    : 6-45跳跃游戏II.py
# @Software: PyCharm

'''

def jump(nums):
    res = 0
    nextD = 0
    curD = 0
    for i in range(len(nums)):
        nextD = max(nums[i] + i, nextD)
        if curD == i and curD != len(nums)-1:
            curD = nextD
            res += 1
            if nextD >= len(nums)-1:
                break
    return res
