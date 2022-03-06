#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/6 9:19
# @Author  : yq
# @File    : 347前k个高频元素.py
# @Software: PyCharm

'''
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
if __name__ == '__main__':
    a = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    temp = a.topKFrequent(nums, k)
    print(temp)
