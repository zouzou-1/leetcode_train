# -*- coding: utf-8 -*-            
# @Time : 2023/1/7 16:30
# @Author: zouying
# @FileName: 150. 逆波兰表达式求值.py
# @Software: PyCharm
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack_num = []
        index = 0
        while index < len(tokens):
            temp = tokens[index]
            if temp == '+':
                temp1 = stack_num.pop()
                temp2 = stack_num.pop()
                stack_num.append(temp1 + temp2)
            elif temp == '-':
                temp1 = stack_num.pop()
                temp2 = stack_num.pop()
                stack_num.append(temp2 - temp1)
            elif temp == '/':
                temp1 = stack_num.pop()
                temp2 = stack_num.pop()
                stack_num.append(int(temp2/temp1))
            elif temp == '*':
                temp1 = stack_num.pop()
                temp2 = stack_num.pop()
                stack_num.append(temp1 * temp2)
            else:
                s = tokens[index]
                num = 0
                x = 1
                index_num = len(tokens[index]) - 1
                while s[index_num] != '-' and index_num >= 0:
                    num += (int(s[index_num])*(x))
                    x *= 10
                    index_num -= 1
                if s[0] == '-':
                    num = num*-1
                stack_num.append(num)
            index += 1
            print(stack_num)
        return  stack_num.pop()
if __name__ == '__main__':
    solution = Solution
    print(solution.evalRPN(solution, ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))