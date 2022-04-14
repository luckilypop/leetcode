#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/14 11:11
# @Author  : yq
# @File    : 8-131分割回文串.py
# @Software: PyCharm

'''
def partition(s):
    path = []
    paths = []
    def backtrack(s,start_index):
        if start_index >= len(s):
            paths.append(path[:])
            return

        for i in range(start_index, len(s)):
            temp = s[start_index:i+1]
            if temp == temp[::-1]:
                path.append(temp)
                backtrack(s, i+1)
                path.pop()
            else:
                continue
    backtrack(s,0)
    return paths

print(partition("aab"))