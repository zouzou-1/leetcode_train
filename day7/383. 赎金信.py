# -*- coding: utf-8 -*-            
# @Time : 2023/1/3 15:27
# @Author: zouying
# @FileName: 383. 赎金信.py
# @Software: PyCharm
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        hashmagzine = {}
        for i in magazine:
            if i in hashmagzine.keys():
                hashmagzine[i] += 1
            else:
                hashmagzine[i] = 1
        for i in ransomNote:
            if i in hashmagzine.keys() and hashmagzine[i] > 0:
                hashmagzine[i] -= 1
            else:
                return False

        return True

if __name__ == '__main__':
    solution = Solution
    print(solution.canConstruct(solution, "aa", "ab"))