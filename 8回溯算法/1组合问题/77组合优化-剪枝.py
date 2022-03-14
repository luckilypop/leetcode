#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/14 11:29
# @Author  : yq
# @File    : 77组合优化-剪枝.py
# @Software: PyCharm

'''
class Solution:
    def combine(self, n, k):
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex,n-(k-len(path))+2):  #优化的地方
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return res
if __name__ == '__main__':
    a = Solution()
    temp = a.combine(4,2)
    print(temp)
