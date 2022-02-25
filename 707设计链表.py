
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
    def initList(self, data):
        # data 不为空时候，创建头结点
        while data:
            # 创建头节点
            self.head = Node(data[0])
            r = self.head  # 头结点
            p = self.head  # 指针
            # p作为指针，逐个为 data 内的数据创建结点, 建立链表
            for i  in data[1:]:
                node = Node(i)
                p.next = node
                p = p.next
            return r

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
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

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            # 计数-1
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None




if __name__ == '__main__':
    a = MyLinkedList()

    a.initList([1,2,3])
    node = a.head
    re = []
    while node != None:
        re.append(node.val)
        node = node.next
    print(re)
