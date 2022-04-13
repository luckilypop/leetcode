#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/13 9:21
# @Author  : yq
# @File    : 4-42接雨水.py
# @Software: PyCharm

'''


def trap(height):
    stack = [0]
    res = 0
    for i in range(1, len(height)):
        if height[i] < height[stack[-1]]:
            stack.append(i)
        elif height[i] == height[stack[-1]]:
            stack.pop()
            stack.append(i)
        else:
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack[-1]]
                stack.pop()
                if stack:
                    right_h = height[i]
                    left_h = height[stack[-1]]
                    h = min(right_h, left_h) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))