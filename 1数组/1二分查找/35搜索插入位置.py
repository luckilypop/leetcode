#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/22 14:34
# @Author  : yq
# @File    : 35搜索插入位置.py
# @Software: PyCharm

'''
# 题目
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#  请必须使用时间复杂度为 O(log n) 的算法。


class Solution:
    # 方法一：左闭右闭
    def searchInsert_1(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            middle = (left + right) //2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle +1
            else:
                right = middle -1
        return right+1 # 结果是right+1


    # 方法2：左闭右开
    def searchInsert_2(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) //2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle +1
            else:
                right = middle
        return right # 结果是right
367