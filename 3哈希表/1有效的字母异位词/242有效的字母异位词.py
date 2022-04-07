#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 18:27
# @Author  : yq
# @File    : 242有效的字母异位词.py
# @Software: PyCharm

'''

# 题目
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 异位词： 两个单词包含相同的字母，但是次序不同
class Solution:
    def isAnagram(self, s, t):
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            record[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if record[i] != 0:
                return False
                break

        return True

    # 方法二：python内置函数
    def isAnagram_2(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    a = Solution()
    temp = a.isAnagram("asdc","asde")
    print("temp:",temp)