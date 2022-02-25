#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/22 15:09
# @Author  : yq
# @File    : 34在排序数组钟查找元素得第一个和最后一个位置.py
# @Software: PyCharm

'''
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。
# 找出给定目标值在数组中的开始位置和结束位置。
#  如果数组中不存在目标值 target，返回 [-1, -1]。
#  进阶：
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

# 解析：
# 寻找target在数组里的左右边界，有如下三种情况：
#
#     情况一：target 在数组范围的右边或者左边，例如数组{3, 4, 5}，target为2或者数组{3, 4, 5},target为6，此时应该返回{-1, -1}
#     情况二：target 在数组范围中，且数组中不存在target，例如数组{3,6,7},target为5，此时应该返回{-1, -1}
#     情况三：target 在数组范围中，且数组中存在target，例如数组{3,6,7},target为6，此时应该返回{1, 1}

class Solution:
    def searchRange(self, nums, target):

        # 寻找右边界
        def getRightboder(nums, target):
            left = 0
            right = len(nums) -1
            rightboder = -2
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] > target:
                    right = middle -1
                else:
                    left = middle + 1
                    rightboder = left
            return rightboder

        # 寻找左边界
        def getLeftboder(nums, target):
            left = 0
            right = len(nums) -1
            leftboder = -2
            while left <= right:
                middle = (left + right) //2
                if nums[middle] >= target:
                    right = middle -1
                    leftboder = right
                else:
                    left = middle +1
            return leftboder


        # 得到左右边界
        leftborder = getLeftboder(nums, target)
        rightboder = getRightboder(nums, target)

        # 情况一：
        if leftborder == -2 or rightboder == -2:
            return [-1,-1]
        # 情况三：
        if rightboder - leftborder > 1:
            return [leftborder+1,rightboder-1]
        # 情况二：
        return [-1,-1]


if __name__ == '__main__':
    a = Solution()
    temp = a.searchRange([5,7,7,8,8,10],8)
    print("temp:",temp)