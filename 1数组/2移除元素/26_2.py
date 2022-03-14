#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/14 9:53
# @Author  : yq
# @File    : 26_2.py
# @Software: PyCharm

'''


class Solution:
    def removeDuplicates(self, nums):
        slow, fast = 0, 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
if __name__ == '__main__':
    a = Solution()
    temp = a.removeDuplicates([1, 1, 2, 2, 3, 4])
    print("temp:", temp)
