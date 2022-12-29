# -*- coding: utf-8 -*-            
# @Time : 2022/12/29 14:33
# @Author: zouying
# @FileName: 59.螺旋矩阵II.py
# @Software: PyCharm
class Solution(object):
    # 考虑惯性
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0 for col in range(n)] for row in range(n)]
        val = 1
        row = 0
        col = 0
        step = 0
        row_step = [0, 1, 0, -1]
        col_step = [1, 0, -1, 0]
        while val <= n * n:
            nums[row][col] = val
            if row+row_step[step] < n and row+row_step[step] >= 0 and\
                    col+col_step[step] < n and col+col_step[step] >= 0 and \
                    nums[row+row_step[step]][col+col_step[step]] == 0:
                row += row_step[step]
                col += col_step[step]
            else:
                step = (step + 1) % 4
                row += row_step[step]
                col += col_step[step]
            val += 1
        return nums
    # 暴力解法：右下左上
    def generateMatrix2(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0 for col in range(n)] for row in range(n)]
        val = 1
        row = 0
        col = 0
        loop, mid = n//2, n//2
        for offset in range(1, loop+1):
            for i in range(col, n-offset):
                nums[row][i] = val
                val += 1
            for i in range(row, n-offset):
                nums[i][n-offset] = val
                val += 1
            for i in range(n-offset, col, -1):
                nums[n-offset][i] = val
                val += 1
            for i in range(n-offset, row, -1):
                nums[i][col] = val
                val += 1
            col += 1
            row += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] =val
        return nums

if __name__ == '__main__':
    solution = Solution
    print(solution.generateMatrix2(solution, 3))
    print(solution.generateMatrix2(solution, 4))
