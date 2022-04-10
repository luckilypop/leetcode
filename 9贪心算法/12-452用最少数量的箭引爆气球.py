#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/10 10:56
# @Author  : yq
# @File    : 12-452用最少数量的箭引爆气球.py
# @Software: PyCharm

'''

def findMinArrowShots(points):
    if len(points) == 0:
        return 0
    points.sort(key=lambda x: x[0])
    res = 1
    for i in range(1, len(points)):
        if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
            res += 1
        else:
            points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界
    return res
