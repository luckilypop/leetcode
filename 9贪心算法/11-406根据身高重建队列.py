#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/9 11:19
# @Author  : yq
# @File    : 11-406根据身高重建队列.py
# @Software: PyCharm

'''

def reconstructQueue(people):
    # 先按照h维度的身高顺序从高到低排序。确定第一个维度
    # lambda返回的是一个元组：- 逆序排序；当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
    people.sort(key=lambda x: (-x[0], x[1]))
    print(people)

    que = []
    # 根据每个元素的第二个维度k，贪心算法，进行插入
    # people已经排序过了：同一高度时k值小的排前面。
    for p in people:
        que.insert(p[1], p)
    return que

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))