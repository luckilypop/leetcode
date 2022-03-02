#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/2 9:56
# @Author  : yq
# @File    : 54翻转函数II.py
# @Software: PyCharm

'''
class Solution:
    def reverseStr(self, s, k) -> str:
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)
        print(res)
        for cur in range(0, len(s), 2*k):
            res[cur: cur + k] = reverse_substring(res[cur:cur+k])
        return "".join(res)
if __name__ == '__main__':
    a = Solution()
    temp = a.reverseStr("abcdefg",2)
    print(temp)
