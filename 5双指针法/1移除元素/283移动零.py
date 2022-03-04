#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/24 8:37
# @Author  : yq
# @File    : 283移动零.py
# @Software: PyCharm

'''
# 题目：
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#  请注意 ，必须在不复制数组的情况下原地对数组进行操作。

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
            # nums.pop() #模拟栈的弹出
        return nums

if __name__ == '__main__':
    a = Solution()
    temp = a.moveZeroes([1,2,0,0,4,0])
    print("temp:", temp)
