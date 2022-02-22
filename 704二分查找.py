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
    def search(self, nums, target):
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

a = Solution()
temp = a.search([-1,2,3,4,5,6,7,10,12],5)
print(temp)