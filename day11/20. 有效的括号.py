# -*- coding: utf-8 -*-            
# @Time : 2023/1/7 12:28
# @Author: zouying
# @FileName: 20. 有效的括号.py
# @Software: PyCharm
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        index = 0
        while index < len(s):
            if s[index] == '(':
                stack.append(')')
            elif s[index]=='[':
                stack.append(']')
            elif s[index]=='{':
                stack.append('}')
            elif s[index] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
            index += 1
        return not stack
    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return True
        if len(s)%2 == 1:
            return False
        index = 0
        while index < len(s):
            if s[index] == '(' or s[index] == '[' or s[index] == '{':
                stack.append(s[index])
            elif len(stack) > 0 :
                if s[index] == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
                elif s[index] == ']' and stack[len(stack)-1] == '[':
                    stack.pop()
                elif s[index] == '}' and stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
            index += 1
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution
    print(solution.isValid(solution, "(]"))