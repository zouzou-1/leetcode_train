# -*- coding: utf-8 -*-            
# @Time : 2023/1/2 11:47
# @Author: zouying
# @FileName: 202. 快乐数.py
# @Software: PyCharm

class Solution(object):
    def getelem(self, n):
        sum = 0
        while n :
            sum += (n%10) ** 2
            n = n//10
        return sum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = set()
        sum = n
        while 1:
            sum = self.getelem(sum)
            if sum == 1:
                return True
            if sum in record:
                break
            record.add(sum)
        return False

    def isHappy1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict = {}
        while 1:
            num_dict[n] = 1
            str_n = str(n)
            sum = 0
            for i in str_n:
                m = ord(i)-ord('0')
                sum += m*m
            n = sum
            if sum == 1:
                return True
            if sum in num_dict.keys():
                break
        return False



if __name__ == '__main__':
    solution = Solution
    print(solution.isHappy(solution, n = 2))
