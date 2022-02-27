#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 19:04
# @Author  : yq
# @File    : 383赎金信.py
# @Software: PyCharm

'''

# 题目
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
#
#  如果可以，返回 true ；否则返回 false 。

class Solution:
    def canConstruct(self, ransomNote, magazine):
        record = [0] * 26
        # 交换顺序
        for i in range(len(magazine)):
            record[ord(magazine[i]) - ord('a')] += 1

        for i in range(len(ransomNote)):
            record[ord(ransomNote[i]) - ord('a')] -= 1


        for i in range(26):
            if record[i] < 0:
                return False
                break
        return True

if __name__ == '__main__':
    a = Solution()
    temp = a.canConstruct("aa","aab")
    print(temp)
