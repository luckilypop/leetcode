#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 22:20
# @Author  : yq
# @File    : 438找到字符串中所有的字母异位词.py
# @Software: PyCharm

'''
class Solution:
    def findAnagrams(self, s, p):
        m, n, ans = len(s), len(p), list()
        if m < n: return ans
        book_s, book_p = [0] * 26, [0] * 26
        for i in range(n):
            book_s[ord(s[i]) - ord('a')] += 1
            book_p[ord(p[i]) - ord('a')] += 1
        for i in range(n, m):
            if book_s == book_p: ans.append(i - n)
            book_s[ord(s[i - n]) - ord('a')] -= 1
            book_s[ord(s[i]) - ord('a')] += 1
        if book_s == book_p: ans.append(m - n)
        return ans

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
    s = "abab"
    p = "ab"
    temp = a.findAnagrams_2(s,p)
    print(temp)
