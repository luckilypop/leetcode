#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/24 19:41
# @Author  : yq
# @File    : 76最小覆盖字串.py
# @Software: PyCharm

'''
# 题目
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

from collections import defaultdict
class Solution:
    def minWindow(self, s, t):

        # defaultdick统计字符串中字母出现的个数
        char_count = defaultdict(int)
        for char in t:
            char_count[char] += 1
        print("---strt1---")
        print("输出char_count:\n",char_count)
        print("---end1----")

        # 如果不用defaultdick的写法如下：
        # char_count ={}
        # for k in t:
        #     if k not in char_count:
        #         char_count[k] = 1
        #     else:
        #         char_count[k] += 1
        # print("---strt2---")
        # print("输出char_count:\n", char_count)
        # print("---end2----")
        #
        if len(s) < len(t):
            return ""

        t_len = len(t)  # 统计当前区间包含t中字母的个数
        min_left, min_right = 0, len(s)
        left = 0
        res = ''
        for right, char in enumerate(s):
            if char_count[char] > 0:
                t_len -= 1
            char_count[char] -= 1
            if t_len == 0:
                while char_count[s[left]] < 0:
                    char_count[s[left]] += 1
                    left += 1
                if right - left < min_right - min_left:
                    min_left, min_right = left, right
                    res = s[min_left:right + 1]
                char_count[s[left]] += 1
                t_len += 1
                left += 1
        return res
if __name__ == '__main__':
    a = Solution()
    temp = a.minWindow("DOBECODEBANC","ABC")
    print("temp:", temp)
