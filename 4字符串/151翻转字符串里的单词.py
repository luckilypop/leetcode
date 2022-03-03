#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/3 8:46
# @Author  : yq
# @File    : 151翻转字符串里的单词.py
# @Software: PyCharm

'''


class Solution:
    # 1.去除多余的空格
    def trim_spaces(selfself, s):
        n = len(s)
        left = 0
        right = n - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        tmp = []
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ': # 数组中-1指最后一位

                tmp.append(s[left])
            left += 1
        return tmp

    # 2.翻转字符数组
    def reverse_string(self,nums,left,right):
         while left<right:
             nums[left],nums[right] = nums[right], nums[left]
             left += 1
             right -= 1
         return None

    # 3.翻转字符串里面每个单词
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start<n:
            while end<n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums,start,end-1)
            start = end+1
            end += 1
        return None
    # 4. 翻转字符串
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse_string(l,0,len(l)-1)
        self.reverse_each_word(l)
        return ''.join(l)
if __name__ == '__main__':
    a = Solution()
    s = " ti is   fos   and you are a girl  "
    temp = a.reverseWords(s)
    print(temp)
