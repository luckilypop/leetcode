#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/6 8:42
# @Author  : yq
# @File    : 150逆波兰表达式求值.py
# @Software: PyCharm

'''
class Solution:
    def evalRPN(self, tokens):
        stack = []
        ans = 0
        for item in tokens:
            if item not in {'+','-','*','/'}:
                stack.append(item)
            else:
                temp1, temp2 = stack.pop(), stack.pop()
                ans = int(eval(f'{temp2} {item} {temp1}')) # 第一个出来的在运算符后面
                stack.append(ans)
        return int(stack.pop()) # 如果一开始只有一个数，那么会是字符串形式的
if __name__ == '__main__':
    a = Solution()
    temp = a.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(temp)
