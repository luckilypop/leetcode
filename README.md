# leetcode

### leetcode刷题——2022.2.22开始

---

## 刷题时间记录
### 【3】2022-2-22：704、34、35
### 【8】2022-2-23：36、367、26、27、69
### 【13】2022-2-24：283、844、977、76、209
### 【18】2022-2-25：59、offer29、203
### 【20】2022-2-26：707、206
### 【31】2022-3-1：1、454、15、18 ----哈希表结束
### 【34】2022-3-2：54、344、offer05
### 【37】2022-3-3：151、offer58II、28
### 【38】2022-3-4：459 ----字符串结束、双指针整理结束
### 【42】2022-3-5：20、225、232、1047
### 【45】2022-3-6：150、239、347 ----栈与队列结束
---

## 二分法

- ### 前提条件: 有序数组  +   无重复数据
- ### 两种方式

  #### 方式一：定义 target 是在一个在左闭右闭的区间里，也就是[left, right]

  #### 方式二：定义 target 是在一个在左闭右开的区间里，也就是[left, right)
- ### 题目：704、34、35、69、367



## 移除元素

- ### 数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖
- ### 两种方式

  #### 方式一：暴力求解，两个for循环

  #### 方式二：双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作
- ### 题目：26、27、283、844



## 有序数组的平方

- ### 两种方式

  #### 方式一：暴力求解，两个for循环

  #### 方式二：双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作
- ### 题目：977



## 长度最小的子数组

- ### 两种方式

  #### 方式一：暴力解法当然是 两个for循环，然后不断的寻找符合条件的子序列，时间复杂度很明显是O(n^2)

  #### 方式二：滑动窗口，就是不断的调节子序列的起始位置和终止位置，从而得出我们要想的结果，O(n)
- ### 题目：209、904、76



## 螺旋矩阵

- ### 模拟顺时针画矩阵的过程:

  #### 填充上行从左到右

  #### 填充右列从上到下

  #### 填充下行从右到左

  #### 填充左列从下到上

  #### 由外向内一圈一圈这么画下去
- - ### 题目：59、offer29



## 链表基础

- ### py构造链表
    ```
  class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
  ```


## 移除链表元素
- ### 两种方式

  #### 方式一：直接使用原来的链表来进行删除操作

  #### 方式二：设置一个虚拟头结点在进行删除操作
- ### 题目：203


## 设计链表
- ### 单链表
- ### 双链表？？？
- ### 题目：707

## 翻转链表
- ### 两种方式
  #### 方式一：双指针法
  #### 方式二：递归法
- ### 题目：206

## 两两交换链表中的结点
- ### 题目：24

## 删除链表的倒数第N个节点
- ### 题目：19

## 链表相交
- ### 题目：面试0207

## 环形链表II
- ### 题目：142

## 哈希表
- ### 定义：哈希表是根据关键码的值而直接进行访问的数据结构

## 有效的字母异位词
- ### 题目：49、242、383、438

## 两个数的交集
- ### 题目：349、350II

## 快乐数
- ### 题目：202