#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/8 14:02
# @Author  : yq
# @File    : 55跳跃游戏.py
# @Software: PyCharm

'''

def canJump(nums):
    # 自己写的算法：
    cover = 0
    for i in range(len(nums)):
        if nums[i] > cover:
            cover = nums[i]
        if cover >= len(nums)-1-i:
            return True
        # 重点这一句
        if cover == 0 and nums[i] == 0 :
            return False
        cover -= 1
    return False

def canJump2(nums):
    cover = 0
    if len(nums) == 1:
        return True
    i = 0
    while i <= cover:
        cover = max(i + nums[i], cover)
        if cover >= len(nums) - 1:
            return True
        i += 1
    return False