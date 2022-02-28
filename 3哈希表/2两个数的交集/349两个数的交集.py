#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/28 9:18
# @Author  : yq
# @File    : 349两个数的交集.py
# @Software: PyCharm

'''
# 题目
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。
# 输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

class Solution:
    def intersection(self, nums1, nums2):
        # 直接的方法：return list(set(nums1) & set(nums2))
        res = []
        record_1, record_2 = [], []

        for i in range(len(nums1)):
            if nums1[i] not in record_1:
                record_1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in record_1:
                if nums2[i] not in res:
                    res.append(nums2[i])

        return res
if __name__ == '__main__':
    a = Solution()
    s = [4,9,5]
    p = [9,4,9,8,4]
    temp = a.intersection(s,p)
    print(temp)
