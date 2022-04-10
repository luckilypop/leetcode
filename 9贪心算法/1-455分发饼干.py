#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/8 13:04
# @Author  : yq
# @File    : 1-455分发饼干.py
# @Software: PyCharm

'''

class Solution:
    def findContentChildren(self, g, s):
        # 考虑胃口，先胃口大的优先
        s.sort()
        g.sort()
        j = len(s)-1
        count = 0
        for i in range(len(g)-1,-1,-1):
            # j>=0 写在前面，否则会超出范围
            if j >= 0 and s[j] >= g[i]:
                count += 1
                j -= 1
        return count
    # 考虑饼干
    def findContentChildren2(self, g, s):
        s.sort()
        g.sort()
        count = 0
        j = 0
        for i in range(len(s)):
            if j < len(g) and s[i] >= g[j]:
                count += 1
                j += 1
        return count
