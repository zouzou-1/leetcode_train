# -*- coding: utf-8 -*-            
# @Time : 2023/1/5 10:21
# @Author: zouying
# @FileName: 28. 找出字符串中第一个匹配项的下标.py
# @Software: PyCharm

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1
        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle) and haystack != needle:
            return -1
        else:
            hay = 0
            nee =0
            while hay < len(haystack)-len(needle) + 1:
                if haystack[hay] == needle[nee]:
                    index = hay
                    flag = 1
                    while nee < len(needle):
                        if haystack[hay] != needle[nee]:
                            hay = index + 1
                            nee = 0
                            flag = 0
                            index = -1
                            break
                        nee += 1
                        hay += 1
                    if flag:
                        return index
                else:
                    nee = 0
                    index = -1
                    hay += 1

        return index

if __name__ == '__main__':
    solution = Solution
    print(solution.strStr(solution, haystack = "mississippi", needle = "sippj"))


