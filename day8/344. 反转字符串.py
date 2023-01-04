# -*- coding: utf-8 -*-            
# @Time : 2023/1/4 17:12
# @Author: zouying
# @FileName: 344. 反转字符串.py
# @Software: PyCharm
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 头尾交换
        if len(s) > 1:
            left = 0
            right = len(s)-1
            while left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1


    def reverseString1(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 操作: 存储，后移一位。
        if len(s) > 1:
            for index in range(1, len(s)):
                temp = s[index]
                for i in range(index, 0, -1):
                    s[i] = s[i-1]
                s[0] = temp



if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    solution = Solution
    solution.reverseString(solution, s)