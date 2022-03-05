#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/5 9:48
# @Author  : yq
# @File    : 20有效括号.py
# @Software: PyCharm

'''
# 方法一，仅使用栈，更省空间
class Solution:
    def isValid(self, s):
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False



if __name__ == '__main__':
    a = Solution()
    temp = a.isValid("{[{]}}")
    print(temp)
