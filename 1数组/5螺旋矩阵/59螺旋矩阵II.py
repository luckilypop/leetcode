#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/25 8:49
# @Author  : yq
# @File    : 59螺旋矩阵II.py
# @Software: PyCharm

'''

# 题目
# 给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，
# 且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

class Solution:
    def generateMatrix(self, n):
        # 初始化矩阵
        matrix  = [[0] * n for _ in range(n)]
        # 边缘设置
        left, right ,up, down = 0, n-1, 0, n-1
        # 需要填充的数字
        number = 1

        while left < right and up < down:

            # 从左填右
            for x in range(left,right):
                matrix[up][x] = number
                number += 1

            # 从上到下
            for y in range(up,down):
                matrix[y][right] = number
                number += 1

            # 从右到左
            for x in range(right,left, -1):
                matrix[down][x] = number
                number += 1

            # 从下到上
            for y in range(down, up , -1):
                matrix[y][left] = number
                number += 1

            # 缩小填充范围
            left += 1
            right -= 1
            up += 1
            down -= 1

        # 如果是奇数，额外填充一次
        if n % 2:
            matrix[n // 2][n // 2] = number

        return matrix




if __name__ == '__main__':
    a = Solution()
    temp = a.generateMatrix(5)
    print("temp:", temp)
