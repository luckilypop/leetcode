#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/24 19:24
# @Author  : yq
# @File    : 904水果成篮.py
# @Software: PyCharm

'''
# 题目
# 求只包含两种元素的最长连续子序列
class Solution:
    def totalFruit(self, fruits):
        k = 0
        basket = [fruits[0]]
        res = 0
        for i in range(len(fruits)):
            if fruits[i] not in basket:
                basket.append(fruits[i])
            if len(basket) > 2:
                k = i - 2
                while fruits[k] == fruits[i-1]:
                    k -= 1
                basket.remove(fruits[k])
                k += 1
            res = max(res, i -k +1)
        return res

if __name__ == '__main__':
    a = Solution()
    temp = a.totalFruit([1,2,3,2,2])
    print("temp:", temp)
