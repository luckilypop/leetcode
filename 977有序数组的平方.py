#!/usr/bin/env python


'''
# @Time    : 2022/2/24 9:06
# @Author  : yq
# @File    : 977有序数组的平方.py
# @Software: PyCharm

'''

# 题目
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
class Solution:

    # 方法一：暴力算法，求解之后排序
    def sortedSquares_1(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort() # python排序函数
        return nums

    # 方法二：双指针方法
    def sortedSquares_2(self, nums):
        n = len(nums)
        i, j , k = 0, n-1, n-1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2

            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans

if __name__ == '__main__':
    a = Solution()
    temp = a.sortedSquares_2([-4,1,2,3])
    print("temp:", temp)
