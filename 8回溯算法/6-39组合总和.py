#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/14 10:57
# @Author  : yq
# @File    : 6-39组合总和.py
# @Software: PyCharm

'''
def combinationSum(candidates, target):
    path = []
    paths = []

    def backtrack(candidates, target, sum_now, start_index):
        if sum_now == target:
            paths.append(path[:])
            return
        if sum_now > target:
            return
        for i in range(start_index, len(candidates)):
            sum_now += candidates[i]
            path.append(candidates[i])
            backtrack(candidates,target,sum_now,i)
            sum_now -= candidates[i]
            path.pop()
    backtrack(candidates,target,0,0)
    return paths

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))