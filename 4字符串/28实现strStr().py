#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/3 9:22
# @Author  : yq
# @File    : 28实现strStr().py
# @Software: PyCharm

'''
class Solution:
    def strStr(self, haystack, needle):
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        p = 0
        for j in range(b):
            while p > 0 and needle[p] != haystack[j]:
                p = next[p-1]
            if needle[p] == haystack[j]:
                p += 1
            if p == a:
                return j - a + 1
        return -1

    def getnext(self, a, needle):
        pre_next= ['' for i in range(a)]
        j = 0
        k = -1
        pre_next[0] = k
        while j < a-1:
            if k==-1 or needle[k]==needle[j]:
                k += 1
                j += 1
                pre_next[j] = k
            else:
                k = pre_next[k]
        return pre_next
if __name__ == '__main__':
    a = Solution()
    temp = a.strStr("abaabaaf","abaaf")
    print(temp)
