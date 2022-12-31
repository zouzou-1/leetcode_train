# -*- coding: utf-8 -*-            
# @Time : 2022/12/31 16:02
# @Author: zouying
# @FileName: 面试题 02.07. 链表相交.py
# @Software: PyCharm
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#  过于麻烦，直接网页敲
# 暴力解法，41/45
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        NewHeadA = ListNode(next=headA)
        NewHeadB = ListNode(next=headB)
        A = NewHeadA
        B = NewHeadB

        while A.next:
            while B.next:
                if A.next == B.next:
                    return A.next
                B = B.next
            B = NewHeadB
            A = A.next
        return None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        NewHeadA = ListNode(next=headA)
        NewHeadB = ListNode(next=headB)
        headFsizeA = NewHeadA
        headFsizeB = NewHeadB
        lengthA = 0
        lengthB = 0
        while headFsizeA.next:
            headFsizeA = headFsizeA.next
            lengthA += 1
        while headFsizeB.next:
            headFsizeB = headFsizeB.next
            lengthB += 1

        if lengthA > lengthB:
            longer = lengthA
            shorter = lengthB
            shorterhead = NewHeadB
            longerhead = NewHeadA
        else:
            longer = lengthB
            shorter = lengthA
            shorterhead = NewHeadA
            longerhead = NewHeadB
        discrepancy = longer - shorter
        while discrepancy:
            longerhead = longerhead.next
            discrepancy -= 1
        while longerhead.next:
            if longerhead.next == shorterhead.next:
                return longerhead.next
            longerhead = longerhead.next
            shorterhead = shorterhead.next
        return None
if __name__ == '__main__':
    dataA = [1, 2, 3, 4, 5]
    linkedListA = MyLinkedList()
    for i in dataA:
        linkedListA.addAtTail(i)
    solution = Solution
    p = linkedListA.head.next
    dataB = [1, 2, 3, 4, 5]
    linkedListB = MyLinkedList()
    for i in dataB:
        linkedListA.addAtTail(i)
    solution = Solution
    p = linkedListA.head.next

    print(solution.removeNthFromEnd(solution, p, 2).val)

