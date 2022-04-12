#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/12 9:25
# @Author  : yq
# @File    : 1-739每日温度.py
# @Software: PyCharm

'''
def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = [0]
    for i in range(1, len(temperatures)):
        if temperatures[i] <= temperatures[stack[-1]]:
            stack.append(i)
        else:
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

    return ans

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))