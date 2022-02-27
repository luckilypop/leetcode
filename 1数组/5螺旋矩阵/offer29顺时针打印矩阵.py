#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/25 9:13
# @Author  : yq
# @File    : offer29顺时针打印矩阵.py
# @Software: PyCharm

'''
# 题目
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
class Solution:
    def spiralOrder(self, matrix):

        if len(matrix) == 0:
            return []
        # 行数
        raw = len(matrix)
        # 列数
        col = len(matrix[0])
        x, y = 0, 0
        res = []
        left, right, up, down = 0, col, 0, raw
        total = 0
        total_num = raw * col

        while True:
            # 走完第一行
            for x in range(left, right):
                res.append(matrix[y][x])
                total += 1
            up += 1
            if total == total_num:
                return res
            # 走完最右列
            for y in range(up, down):
                res.append(matrix[y][x])
                total += 1
            right -= 1
            if total == total_num:
                return res

            for x in range(right-1, left-1, -1):
                res.append(matrix[y][x])
                total += 1
            down -= 1
            if total == total_num:
                return res

            for y in range(down-1, up-1, -1):
                res.append(matrix[y][x])
                total += 1
            left += 1
            if total == total_num:
                return res

if __name__ == '__main__':
    a = Solution()
    temp = a.spiralOrder([[2,3,4,5], [5,6,7,8], [2,3,4,5]])
    print("temp:", temp)
