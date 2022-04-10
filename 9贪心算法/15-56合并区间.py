#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/10 11:30
# @Author  : yq
# @File    : 15-56合并区间.py
# @Software: PyCharm

'''
def merge(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[0])
    result = []
    result.append(intervals[0])
    for i in range(1, len(intervals)):
        last = result[-1]
        if last[1] >= intervals[i][0]:
            result[-1] = [last[0], max(last[1], intervals[i][1])]
        else:
            result.append(intervals[i])
    return result

intervals =[[1,4],[0,4]]
print(merge(intervals))