# -*- coding: utf-8 -*-            
# @Time : 2023/1/2 10:55
# @Author: zouying
# @FileName: 242. 有效的字母异位词.py
# @Software: PyCharm
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = [0]*26
        t_list = [0]*26
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            s_list[ord(i)-ord('a')] += 1 # ord函数得出对应Ascii
            t_list[ord(j)-ord('a')] += 1
        for index in range(0,25):
            if s_list[index] != t_list[index]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution
    print(solution.isAnagram(solution, s = "anagram", t = "nagaram"))
