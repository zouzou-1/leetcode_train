# -*- coding: utf-8 -*-            
# @Time : 2022/12/31 15:17
# @Author: zouying
# @FileName: 19. 删除链表的倒数第 N 个结点.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time : 2022/12/30 14:27
# @Author: zouying
# @FileName: 206. 反转链表.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode()
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
        NewNode = ListNode(val, next=self.head.next)
        self.head.next = NewNode
        self.length += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        NewNode = ListNode(val)
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
        elif index > self.length:
            pass
        else:
            NewNode = ListNode(val)
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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newheadFdelete = ListNode(next=head)
        NewHead =newheadFdelete
        prev = NewHead
        post = NewHead
        while post.next:
            if n:
                post = post.next
                n -= 1
            else:
                post = post.next
                prev = prev.next
        prev.next = prev.next.next
        return newheadFdelete.next

        def removeNthFromEnd1(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            newheadFsize = ListNode(next=head)
            newheadFdelete = ListNode(next=head)
            NewHead = newheadFdelete
            size = 0
            while newheadFsize.next:
                size += 1
                newheadFsize = newheadFsize.next
            index = size - n
            while newheadFdelete.next:
                if index == 0:
                    newheadFdelete.next = newheadFdelete.next.next
                    break
                index -= 1
                newheadFdelete = newheadFdelete.next
            return NewHead.next

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    linkedList = MyLinkedList()
    for i in data:
        linkedList.addAtTail(i)
    solution = Solution
    p = linkedList.head.next
    q = solution.removeNthFromEnd(solution, p, 2)
    while q != None:
        print(q.val)
        q = q.next
