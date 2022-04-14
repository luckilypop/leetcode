#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/14 10:39
# @Author  : yq
# @File    : 5-17电话号码的字母组合.py
# @Software: PyCharm

'''

class Solution:
    def __init__(self):
        self.res = []
        self.ans = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        self.res.clear()
        if not digits:
            return self.res

        self.backtrack(digits,0)
        return self.res

    def backtrack(self, digits, index):
        if index == len(digits):
            self.res.append(self.ans)
            return
        letters: str = self.letter_map[digits[index]]
        for leeter in letters:
            self.ans += leeter
            self.backtrack(digits,index+1)
            self.ans = self.ans[:-1]


a = Solution()
print(a.letterCombinations('23'))