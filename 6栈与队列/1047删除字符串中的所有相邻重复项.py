#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/5 9:55
# @Author  : yq
# @File    : 1047删除字符串中的所有相邻重复项.py
# @Software: PyCharm

'''
class Solution:
    def removeDuplicates(self, s):
        stack = []
        for item in s:
            if stack == []:
                stack.append(item)
            elif item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)
if __name__ == '__main__':
    a = Solution()
    temp = a.removeDuplicates("abbaca")
    print(temp)
