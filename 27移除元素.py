#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/23 10:09
# @Author  : yq
# @File    : 27移除元素.py
# @Software: PyCharm

'''

# 题目
# # 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
class Solution:

    # 方法一：暴力求解
    # 时间复杂度：O(n^2)
    # 空间复杂度：O(1)
    def removeElement_1(self, nums, val):
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == val:
                for j in range(i+1,size):
                    nums[j-1] = nums[j]
                i = i -1
                size = size -1
            i = i+1
        return size

    # 方法二：快慢指针
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def removeElement_2(self, nums, val):
        slow = fast = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow




if __name__ == '__main__':
    a = Solution()
    temp = a.removeElement_1([3,2,1,3],3)
    print("temp:", temp)

