# -*- coding: utf-8 -*-            
# @Time : 2022/12/30 9:57
# @Author: zouying
# @FileName: 203. 移除链表元素.py
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p_prev = ListNode(next = head) #创建和赋值
        p_cur = p_prev.next
        p_rem = p_prev
        while p_cur != None:
            if p_cur.val == val:
                p_prev.next = p_cur.next
                p_cur = p_cur.next
            else:
                p_prev = p_prev.next
                p_cur = p_cur.next
        return p_rem.next

if __name__ == '__main__':

    solution = Solution
    print(solution.removeElements(solution, [1,2,6,3,4,5,6], 6))
    print(solution.removeElements(solution, [], 1))
    print(solution.removeElements(solution, [7, 7, 7, 7], 7))