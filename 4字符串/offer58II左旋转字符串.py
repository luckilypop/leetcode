#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/3 9:18
# @Author  : yq
# @File    : offer58II左旋转字符串.py
# @Software: PyCharm

'''
class Solution:
    def reverseLeftWords(self, s, n):
        # 1. 定义reverse函数，可以使用内建函数reversed
        def reverse_sub(lst,left,right):
            while left < right:
                lst[left],lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        res = list(s)
        end = len(s) - 1
        # 2.翻转前n个数
        reverse_sub(res,0,n-1)
        # 3.翻转后面的数
        reverse_sub(res,n,end)
        # 4.翻转整体的数
        reverse_sub(res,0,end)

        return ''.join(res)

if __name__ == '__main__':
    a = Solution()
    temp = a.reverseLeftWords("abcdefg",2)
    print(temp)
