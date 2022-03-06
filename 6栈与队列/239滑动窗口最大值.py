#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/6 8:54
# @Author  : yq
# @File    : 239滑动窗口最大值.py
# @Software: PyCharm

'''
class MyQueue:
    def __init__(self):
        self.queue = []
    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
    def push(self,value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    def front(self):
        return self.queue[0]
class Solution:
    def maxSlidingWindow(self, nums, k):
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k,len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        return result
if __name__ == '__main__':
    a = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    temp = a.maxSlidingWindow(nums,k)
    print(temp)
