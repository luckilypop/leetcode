#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/13 9:42
# @Author  : yq
# @File    : 5-84柱状图中最大的矩形.py
# @Software: PyCharm

'''
def largestRectangleArea(heights):
    # 输入数组首尾各补上一个0（与42.接雨水不同的是，本题原首尾的两个柱子可以作为核心柱进行最大面积尝试
    heights.insert(0, 0)
    heights.append(0)
    stack = [0]
    res = 0
    for i in range(1, len(heights)):
        if heights[i] > heights[stack[-1]]:
            stack.append(i)
        elif heights[i] == heights[stack[-1]]:
            stack.pop()
            stack.append(i)
        else:
            while stack and heights[i] < heights[stack[-1]]:
                mid = heights[stack[-1]]
                stack.pop()
                if stack:
                    left = stack[-1]
                    right = i
                    w = right - left - 1
                    h = mid
                    res = max(res, w * h)
            stack.append(i)
    return res