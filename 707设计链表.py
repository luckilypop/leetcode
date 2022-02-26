
# encoding: utf-8

'''
# @Time    : 2022/2/25 13:52
# @Author  : yq
# @File    : 707设计链表.py
# @Software: PyCharm

'''


# 单链表
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head = Node(0)  # 虚拟头部节点
        self._count = 0  # 添加的节点数


    # get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    def get(self, index):
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1


    # addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    def addAtHead(self, val):
        self.addAtIndex(0, val)

    # addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
    def addAtTail(self, val):
        self.addAtIndex(self._count, val)

    # addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
    # 如果 index 等于链表的长度，则该节点将附加到链表的末尾。
    # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return

            # 计数累加
        self._count += 1

        add_node = Node(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node

    # deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
    def deleteAtIndex(self, index):
        if 0<= index < self._count:
            # 计数减一
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node, current_node.next




if __name__ == '__main__':
    a = MyLinkedList()
    a.addAtIndex(0,1)
    a.addAtIndex(1,2)
    a.addAtIndex(2,3)

    cur = a._head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print("add之后：",res)

    a.addAtHead(5)
    a.addAtTail(7)
    print(a.get(3))
    cur = a._head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print("add之后：", res)
