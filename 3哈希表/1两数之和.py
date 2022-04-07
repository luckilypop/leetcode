#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/1 9:13
# @Author  : yq
# @File    : 1两数之和.py
# @Software: PyCharm

'''
# 给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
class Solution:
    def twoSum(self, nums, target):
        record = dict()
        for idx, val in enumerate(nums):
            if target - val not in record:
                record[val] = idx
            else:

                return [record[target - val], idx]
if __name__ == '__main__':
    a = Solution()
    temp = a.twoSum([2,4,6,8,7],9)
    print(temp)
