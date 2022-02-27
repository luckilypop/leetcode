#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/24 9:51
# @Author  : yq
# @File    : 209长度最小的子数组.py
# @Software: PyCharm

'''

# 题目
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
# 度。如果不存在符合条件的子数组，返回 0 。
class Solution:

    # 方法一：暴力求解
    def minSubArrayLen_1(self, target, nums):
        result = float("inf")
        sum = 0
        sublenth = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= target:
                    sublenth = j - i + 1
                    result = result if result < sublenth else sublenth
                    break
        return 0 if result ==float("inf") else result

    # 方法二：滑动窗格
    def minSubArrayLen_2(self, target, nums):
        res = float("inf")
        index = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:  # while 非if
                res = min(res, i-index+1)
                sum -= nums[index]
                index += 1
        return 0 if res == float("inf") else res

if __name__ == '__main__':
    a = Solution()
    temp = a.minSubArrayLen_2(5,[1,2,4,3,2])
    print("temp:", temp)
