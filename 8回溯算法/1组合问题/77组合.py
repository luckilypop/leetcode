#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/14 10:46
# @Author  : yq
# @File    : 77组合.py
# @Software: PyCharm

'''
class Solution:
    def combine(self, n, k):
        res = []
        path = []
        def backtrack(n,k,startindex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startindex,n+1):
                path.append(i)
                backtrack(n,k,i+1)
                path.pop()
        backtrack(n,k,1)
        return res


if __name__ == '__main__':
    a = Solution()
    temp = a.combine(4,2)
    print(temp)
