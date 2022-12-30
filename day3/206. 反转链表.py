# -*- coding: utf-8 -*-            
# @Time : 2022/12/30 14:27
# @Author: zouying
# @FileName: 206. 反转链表.py
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

class Solution(object):

    # 迭代法
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(cur, pre):
            if cur == None:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(temp, cur)
        return reverse(head, None)
    # 迭代法
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre = None
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur =temp
        return pre

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next != None:
            NewHead = self.reverseList(self, head.next)
            NewNode = LinkNode(head.val)
            NewTail = NewHead
            while NewTail.next != None:
                NewTail = NewTail.next
            NewTail.next = NewNode
        elif head.next == None:
            NewHead = LinkNode(head.val)
        return NewHead


if __name__ == '__main__':
    data = [1,2,3,4,5]
    linkedList = MyLinkedList()
    for i in data :
        linkedList.addAtTail(i)
    solution = Solution
    p = linkedList.head.next
    q=solution.reverseList(solution, p)
    while q != None:
        print(q.val)
        q=q.next
