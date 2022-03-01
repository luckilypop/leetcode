#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/1 9:23
# @Author  : yq
# @File    : 454四数相加II.py
# @Software: PyCharm

'''
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
# 使得 A[i] + B[j] + C[k] + D[l] = 0。
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                k = -n3-n4
                if k in hashmap:
                    count += hashmap[k]
        return count
if __name__ == '__main__':
    a = Solution()
    temp = a.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])
    print(temp)
