# -*- coding: utf-8 -*-            
# @Time : 2023/1/4 19:35
# @Author: zouying
# @FileName: 剑指 Offer 05. 替换空格.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time : 2023/1/4 18:04
# @Author: zouying
# @FileName: 541. 反转字符串 II.py
# @Software: PyCharm

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        news = ""
        for i in s:
            if i == " ":
                news += "%20"
            else:
                news += i
        return news

if __name__ == '__main__':
    solution = Solution
    print(solution.replaceSpace(solution, "We are happy."))