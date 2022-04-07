#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 21:55
# @Author  : yq
# @File    : 49字母异位分组.py
# @Software: PyCharm

'''
# 题目
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
#  字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            #   sorted(s) = 'a' 'e' 't'
            keys = "".join(sorted(s))


            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())

if __name__ == '__main__':
    a = Solution()
    temp = a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(temp)
