#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/2 9:31
# @Author  : yq
# @File    : 344反转字符串.py
# @Software: PyCharm

'''
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s
if __name__ == '__main__':
    a = Solution()
    temp = a.reverseString(["h","e","l","l","o"])
    print(temp)
