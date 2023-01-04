# -*- coding: utf-8 -*-            
# @Time : 2023/1/4 18:04
# @Author: zouying
# @FileName: 541. 反转字符串 II.py
# @Software: PyCharm

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        news = ""
        index = 0
        while index < len(s):
            left = index
            right = min(len(s)-1, index + k - 1)
            while right >= left:
                news += s[right]
                right -= 1
            if index+k -1 < len(s)-1:
                if index + 2*k <= len(s) -1 :
                    news += s[index + k : index + 2*k]
                    index += 2*k
                elif index + 2*k > len(s) -1 :
                    news += s[index + k: len(s)]
                    break
            else:
                break
        return news

if __name__ == '__main__':
    solution = Solution
    print(solution.reverseStr(solution, "a", 4))