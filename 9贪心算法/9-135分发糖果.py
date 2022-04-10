#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/9 10:57
# @Author  : yq
# @File    : 9-135分发糖果.py
# @Software: PyCharm

'''

def candy(ratings):
    # 从右往左:如果右边大于左边，则右边糖果+1
    candyVec = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candyVec[i] = candyVec[i-1] + 1
    # 从左往右:如果左边大于右边，则左边糖果max
    for i in range(len(ratings)-1,0,-1):
        if ratings[i-1] > ratings[i]:
            candyVec[i-1] = max(candyVec[i-1],candyVec[i]+1)
    return sum(candyVec)