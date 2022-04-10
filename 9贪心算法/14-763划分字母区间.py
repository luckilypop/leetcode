#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/10 11:18
# @Author  : yq
# @File    : 14-763划分字母区间.py
# @Software: PyCharm

'''

def partitionLabels(s):
    hash = [0] * 26
    # 统计每个字符串出现的最后位置
    for i in range(len(s)):
        hash[ord(s[i]) - ord('a')] = i
    res = []
    left = 0
    right = 0
    for i in range(len(s)):
        right = max(right, hash[ord(s[i]) - ord('a')])
        if i == right:
            res.append(right-left+1)
            left = i + 1
    return res