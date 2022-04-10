#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/10 11:06
# @Author  : yq
# @File    : 13-435无重叠区间.py
# @Software: PyCharm

'''

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key = lambda x:x[1])

    count = 1 # 记录非交叉区间的个数
    end = intervals[0][1] # 记录区间分割点
    for i in range(1,len(intervals)):
        if end <= intervals[i][0]:
            count += 1
            end = intervals[i][1]
    return len(intervals) - count

def eraseOverlapIntervals2(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    # 记录删除的个数
    count = 0
    # 记录区间分割点
    end = intervals[0][1]

    for i in range(1,len(intervals)):
        if end > intervals[i][0]:
            count += 1
            end = min(intervals[i][1],end)
        else:
            end = intervals[i][1]
    return count