#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/24 8:58
# @Author  : yq
# @File    : 844比较含退格的字符串.py
# @Software: PyCharm

'''

# 题目
# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
#  注意：如果对空文本输入退格字符，文本继续为空。

class Solution:
    ## 借鉴栈
    def get_string(self, s):
        bz = []
        for i in range(len(s)):
            if s[i] != '#':
                bz.append(s[i])
            elif len(bz) > 0:
                bz.pop()
        return str(bz)

    def backspaceCompare(self, s, t):
        return self.get_string(s) == self.get_string(t)

if __name__ == '__main__':
    a = Solution()
    temp = a.backspaceCompare('abc', 'abb#c')
    print("temp:", temp)
