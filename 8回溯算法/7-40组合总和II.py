#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/14 11:05
# @Author  : yq
# @File    : 7-40组合总和II.py
# @Software: PyCharm

'''
def combinationSum2(candidates, target):
    path = []
    paths = []
    candidates.sort()

    def backtrack(candidates, target, sum_now, start_index):
        if sum_now == target:
            paths.append(path[:])
            return

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i-1]:
                continue

            sum_now += candidates[i]
            path.append(candidates[i])
            backtrack(candidates,target,sum_now,i+1)
            path.pop()
            sum_now -= candidates[i]
    backtrack(candidates,target,0,0)
    return paths

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates,target))