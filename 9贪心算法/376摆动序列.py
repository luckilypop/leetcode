
#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/8 13:15
# @Author  : yq
# @File    : 376摆动序列.py
# @Software: PyCharm

'''

def wiggleMaxLength(nums):
    # 不能设定preC为差值，因为可能只有一个数
    # preC =  nums[1] - nums[0]

    preC, curC, res = 0, 0, 1
    for i in range(len(nums)-1):
        curC = nums[i+1] - nums[i]
        # 因为刚开始设定为preC=0，所以为了第一步成立要《=0
        if preC * curC <= 0 and curC != 0:
            res += 1
            preC = curC
    return res

a = [1,7,4,9,2,5]
b = wiggleMaxLength(a)
print(b)