# -*- coding: utf-8 -*-            
# @Time : 2023/1/7 12:53
# @Author: zouying
# @FileName: 1047. 删除字符串中的所有相邻重复项.py
# @Software: PyCharm
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        slow = fast = 0
        length = len(res)
        while fast < length:
            res[slow] = res[fast]
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0: slow])


    def removeDuplicates1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：一直删除直到栈为空
        if len(s) == 0:
            return s
        stack = []
        stack.append(s[0])
        index = 1
        while index < len(s):
            if stack and s[index] == stack[len(stack)-1]:
                stack.pop()
                index += 1
            elif not stack or s[index] != stack[len(stack)-1]:
                stack.append(s[index])
                index += 1
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution
    print(solution.removeDuplicates(solution, "abbaca"))