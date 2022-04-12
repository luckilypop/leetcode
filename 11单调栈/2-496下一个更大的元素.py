#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/12 9:48
# @Author  : yq
# @File    : 2-496下一个更大的元素.py
# @Software: PyCharm

'''

def nextGreaterElement(nums1, nums2):
    res = [-1] * len(nums1)
    stack = [0]
    for i in range(1, len(nums2)):
        if nums2[i] <= nums2[stack[-1]]:
            stack.append(i)
        else:
            while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                if nums2[stack[-1]] in nums1:
                    index = nums1.index(nums2[stack[-1]])
                    res[index] = nums2[i]
                stack.pop()
            stack.append(i)
    return res


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1,nums2))