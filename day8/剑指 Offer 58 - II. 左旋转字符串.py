# -*- coding: utf-8 -*-            
# @Time : 2023/1/4 20:27
# @Author: zouying
# @FileName: 剑指 Offer 58 - II. 左旋转字符串.py
# @Software: PyCharm
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        slist = list(s)
        if n < len(s):
            # 反转前n个。
            left = 0
            right = n-1
            while left < right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
            # 反转整个字符串
            left = 0
            right = len(slist) - 1
            while left < right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
            #反转前 len(slist)-n 个
            left = 0
            right = len(slist) - n - 1
            while left < right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
        return ''.join(slist)
    def reverseLeftWords2(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        slist = list(s)
        if n < len(s):
            for index in range(0, n):
                temp = slist[0]
                for i in range(0, len(slist)-1):
                    slist[i] = slist[i+1]
                slist[len(slist)-1] = temp
        return ''.join(slist)
    def reverseLeftWords1(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        slist = list(s)
        if n < len(s):
            changelist = slist[0:n]
            rlist = slist[n:]+changelist
        else:
            rlist = slist
        return ''.join(rlist)
if __name__ == '__main__':
    solution = Solution
    print(solution.reverseLeftWords(solution, s = "abcdefg", n = 2))