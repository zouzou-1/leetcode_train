# -*- coding: utf-8 -*-            
# @Time : 2022/12/30 11:46
# @Author: zouying
# @FileName: 707. 设计链表.py
# @Software: PyCharm
class LinkNode(object):
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = LinkNode()
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        search = self.head
        temp = -1
        while search != None:
            if temp == index:
                return search.val
            temp += 1
            search = search.next

        return -1


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        NewNode = LinkNode(val, next = self.head.next)
        self.head.next = NewNode
        self.length += 1



    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        NewNode = LinkNode(val)
        tail = self.head
        while tail.next != None:
            tail = tail.next
        tail.next = NewNode
        self.length += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.length:
            self.addAtTail(val)
        elif index < 0:
            self.addAtHead(val)
        elif index >self.length:
            pass
        else:
            NewNode = LinkNode(val)
            addr = self.head
            while index > 0:
                addr = addr.next
                index -= 1
            NewNode.next = addr.next
            addr.next = NewNode
            self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        search = self.head
        temp = -1
        while search.next != None:
            if temp == index - 1:
                search.next = search.next.next
                self.length -= 1
                break
            temp += 1
            search = search.next






if __name__ == '__main__':
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    linkedList.get(1)
    linkedList.deleteAtIndex(1)
    print(linkedList.get(1))
    p = linkedList.head.next
    while p != None:
        print(p.val)
        p=p.next
