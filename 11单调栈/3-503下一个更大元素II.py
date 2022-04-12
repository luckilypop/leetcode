#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/12 10:10
# @Author  : yq
# @File    : 3-503下一个更大元素II.py
# @Software: PyCharm

'''
def nextGreaterElements(nums):
    dp = [-1] * len(nums)
    stack = []
    for i in range(len(nums*2)):
        while (len(stack) != 0 and nums[i % len(nums)] > nums[stack[-1]]):
            dp[stack[-1]] = nums[i % len(nums)]
            stack.pop()
        stack.append(i % len(nums))
    return dp

print(nextGreaterElements([1,2,1]))