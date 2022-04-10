#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/9 11:08
# @Author  : yq
# @File    : 10-860柠檬水找零.py
# @Software: PyCharm

'''

def lemonadeChange(bills):
    five, ten, twenty = 0, 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        if bill == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False
        if bill == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -=1
                twenty += 1
            elif five > 2:
                five -= 3
            else:
                return False
    return True

