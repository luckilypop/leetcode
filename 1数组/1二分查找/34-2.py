#!/usr/bin/env python


'''
# @Time    : 2022/3/14 9:14
# @Author  : yq
# @File    : 34-2.py
# @Software: PyCharm

'''


class Solution:
    def searchRange(self, nums, target):
        # 借鉴35题目，找到插入那个位置

        def getmid(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return -1

        temp = getmid(nums, target)
        if temp == -1:
            return [-1, -1]
        else:
            left, right = temp, temp
            for i in range(temp + 1, len(nums)):
                if nums[i] == target:
                    right = i
                else:
                    break
            for i in range(temp - 1, -1, -1):
                if nums[i] == target:
                    left = i
                else:
                    break
        return [left, right]
if __name__ == '__main__':
    a = Solution()
    temp = a.searchRange([1,2,2],2)
    print(temp)
