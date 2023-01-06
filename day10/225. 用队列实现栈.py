# -*- coding: utf-8 -*-            
# @Time : 2023/1/6 20:01
# @Author: zouying
# @FileName: 225. 用队列实现栈.py
# @Software: PyCharm
import collections
import collections


class MyStack(object):

    def __init__(self):
        self.queue = collections.deque()
        self.length = 0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.appendleft(x)
        self.length += 1


    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        temp = self.length
        while temp > 1:
            self.queue.appendleft(self.queue.pop())
            temp -= 1
        ans = self.queue.pop()
        self.length -= 1
        return ans

    def top(self):
        """
        :rtype: int
        """
        ans = self.pop()
        self.push(ans)
        return ans

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue


class MyStack1(object):

    def __init__(self):
        self.queue_in = collections.deque()
        self.queue_out = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_in.appendleft(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        if len(self.queue_out) > 0:
            ans = self.queue_out.pop()
            return ans
        else:
            while len(self.queue_in) > 1:
                self.queue_out.appendleft(self.queue_in.pop())
            ans = self.queue_in.pop()
            while self.queue_out:
                self.queue_in.appendleft(self.queue_out.pop())
            return ans

    def top(self):
        """
        :rtype: int
        """
        ans = self.pop()
        self.push(ans)
        return ans

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.queue_in or self.queue_out)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())