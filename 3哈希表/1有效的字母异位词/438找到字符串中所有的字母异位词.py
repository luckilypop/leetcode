#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 22:20
# @Author  : yq
# @File    : 438找到字符串中所有的字母异位词.py
# @Software: PyCharm

'''
# 题目
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
#  异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

class Solution:
    def findAnagrams(self, s, p):

        m, n , res =len(s), len(p), list()

        if m < n:
            return res
        record_s, record_p = [0] * 26, [0] * 26
        for i in range(n):
            record_s[ord(s[i]) - ord('a')] += 1
            record_p[ord(p[i]) - ord('a')] += 1

        for i in range(n, m):
            if record_s == record_p:
                res.append(i-n)

            record_s[ord(s[i-n]) - ord('a')] -= 1
            record_s[ord(s[i]) - ord('a')] += 1

        if record_s == record_p:
            res.append(m-n)
        return res

    def findAnagrams_2(self, s, p):
        lens, lenp, out = len(s), len(p), []
        liss, lisp = [], []
        if lens < lenp:
            return out
        for i in range(lens):
            liss.append(s[i])
            if i < lenp:
                lisp.append(p[i])
        lisp.sort()
        for j in range(lens - lenp + 1):
            subliss = sorted(liss[j:j+lenp])
            if subliss == lisp:
                out.append(j)
        return out

if __name__ == '__main__':
    a = Solution()
    s = "abcab"
    p = "ab"
    temp = a.findAnagrams(s,p)
    print(temp)
