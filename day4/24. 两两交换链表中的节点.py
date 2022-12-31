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


class Solution(object):
    # 简单模拟 虚拟头结点非常重要。以及NULL or 1 个节点的链表要单独讨论
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        NewHead = ListNode()
        NewHead.next = head
        if head == None or head.next == None:
            return head
        else:
            ppre = NewHead ##important
            pre = head
            cur = head.next
            while cur != None:
                temp = cur.next
                cur.next = pre
                pre.next = temp
                ppre.next = cur ## important
                if temp == None or temp.next == None:
                    break
                else:
                    ppre = pre ## important
                    pre = temp
                    cur = temp.next
            return NewHead.next


# 随想录解法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        NewHead = ListNode(next=head)
        cur = NewHead

        while cur.next and cur.next.next:
            pre = cur
            cur = cur.next
            post = cur.next
            temp = cur.next.next

            pre.next = post
            post.next = cur
            cur.next = temp

            cur = pre.next.next

        return NewHead.next


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    linkedList = MyLinkedList()
    for i in data:
        linkedList.addAtTail(i)
    solution = Solution
    p = linkedList.head.next
    q = solution.swapPairs(solution, p)
    while q != None:
        print(q.val)
        q = q.next
