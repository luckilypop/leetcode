#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/2 10:04
# @Author  : yq
# @File    : offer05替换空格.py
# @Software: PyCharm

'''
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

class Solution:
    def replaceSpace(self, s):
        # count = 0
        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         count += 1
        count = s.count(' ') # 完全等于以上代码
        res = list(s)

        res.extend([' '] * count * 2)

        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right - 2:right + 1] = '%20'
                right -= 3
            left -= 1
        return "".join(res)

if __name__ == '__main__':
    a = Solution()
    temp = a.replaceSpace('abc de f')
    print(temp)
