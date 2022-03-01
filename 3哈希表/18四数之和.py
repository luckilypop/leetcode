#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/1 9:58
# @Author  : yq
# @File    : 18四数之和.py
# @Software: PyCharm

'''
class Solution:
    def fourSum(self, nums, target):
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                left = j+1
                right = n-1
                while left < right:
                    tatal = nums[i]+nums[j]+nums[left]+nums[right]
                    if tatal < target:
                        left += 1
                    elif tatal > target:
                        right -= 1
                    else:
                        if [nums[i],nums[j],nums[left],nums[right]] not in ans:
                            ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
        return ans
if __name__ == '__main__':
    a = Solution()
    temp = a.fourSum([1,0,-1,0,-2,2],0)
    print(temp)
