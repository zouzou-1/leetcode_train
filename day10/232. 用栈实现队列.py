# -*- coding: utf-8 -*-            
# @Time : 2023/1/6 19:28
# @Author: zouying
# @FileName: 232. 用栈实现队列.py
# @Software: PyCharm
class MyQueue(object):

    def __init__(self):
        self.stacka = []
        self.stackb = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stacka.append(x)


    def pop(self):
        """
        :rtype: int
        """
        index = len(self.stacka)-1
        while index >= 0:
            self.stackb.append(self.stacka[index])
            index -= 1
        self.stacka.clear()
        rnum = self.stackb[len(self.stackb)-1]
        self.stackb.pop()
        index = len(self.stackb)-1
        while index >= 0:
            self.stacka.append(self.stackb[index])
            index -= 1
        self.stackb.clear()
        return rnum

    def peek(self):
        """
        :rtype: int
        """
        index = len(self.stacka)-1
        while index >= 0:
            self.stackb.append(self.stacka[index])
            index -= 1
        rnum = self.stackb[len(self.stackb) - 1]
        self.stackb.clear() # 注leetcode下，只能使用self.stackb = []
        return rnum

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stacka) == 0:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())