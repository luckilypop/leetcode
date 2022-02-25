#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/23 10:47
# @Author  : yq
# @File    : 26删除有序数组中的重复项.py
# @Software: PyCharm

'''

class Solution:
    def removeDuplicates(self, nums):
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast-1] != nums[fast]:
                nums[slow] = nums[fast-1]
                slow += 1
            fast += 1
        return slow+1

if __name__ == '__main__':
    a = Solution()
    temp = a.removeDuplicates([1,1,2,2,3,4])
    print("temp:", temp)
