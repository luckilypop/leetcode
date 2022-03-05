#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/5 9:16
# @Author  : yq
# @File    : 232用栈实现队列.py
# @Software: PyCharm

'''

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []


    def push(self, x):
        self.stack_in.append(x)



    def pop(self):
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self):
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self):
        return not (self.stack_in or self.stack_out)

if __name__ == '__main__':
    a = MyQueue()
    a.push(3)
    a.push(4)
    a.push(5)
    a.push(6)
    a.push(7)
    print(type(a))
    a.pop()
    a.peek()
    a.empty()
    print(a.stack_out)

