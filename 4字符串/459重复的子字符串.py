#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/4 10:21
# @Author  : yq
# @File    : 459重复的子字符串.py
# @Software: PyCharm

'''
class Solution:
    def repeatedSubstringPattern(self, s):
        if len(s) == 0:
            return False
        pre_next = [0] * len(s)
        pre_next = self.getNext(pre_next,s)
        if pre_next[-1] != 0 and len(s) % (len(s)-pre_next[-1]) == 0:
            return True
        return False
    def getNext(self, pre_next, s):
        pre_next[0] = 0
        j =0
        for i in range(1, len(s)):
            while j >0 and s[i] != s[j]:
                j = pre_next[j-1]
            if s[i] == s[j]:
                j += 1
            pre_next[i] = j
        return pre_next

if __name__ == '__main__':
    a = Solution()
    temp = a.repeatedSubstringPattern("abab")
    print(temp)
