#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/1 9:38
# @Author  : yq
# @File    : 15三数之和.py
# @Software: PyCharm

'''
class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            left = i+1
            right = n -1
            while left < right:
                tatol = nums[i] + nums[left] + nums[right]
                if tatol < 0:
                    left += 1
                elif tatol > 0:
                    right -= 1
                else:
                    if [nums[i],nums[left],nums[right]] not in ans:
                        ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
        return ans
if __name__ == '__main__':
    a = Solution()
    temp = a.threeSum([-1,0,1,2,-1,-4])
    print(temp)
