#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/22 11:00
# @Author  : yq
# @File    : 704二分查找.py
# @Software: PyCharm

'''

# 题目
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否
# 则返回 -1。


class Solution:
    # 方法一：左闭右闭
    def search_1(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    # 方法2：左闭右开
    def search_2(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle + 1   # target 在右边区间
        return -1




