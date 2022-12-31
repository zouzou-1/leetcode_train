# -*- coding: utf-8 -*-            
# @Time : 2022/12/31 19:31
# @Author: zouying
# @FileName: 142. 环形链表 II.py
# @Software: PyCharm

## 暴力解法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(next = head)
        cur = newhead
        nodelist = []
        while cur.next:
            for i in nodelist:
                if i == cur.next:
                    return i
            nodelist.append(cur.next)
            cur = cur.next
        return None

## 空间复杂度为O(1)解法

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                #你也可以return q
                return p

        return None