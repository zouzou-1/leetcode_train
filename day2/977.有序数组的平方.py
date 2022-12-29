# -*- coding: utf-8 -*-            
# @Time : 2022/12/29 12:33
# @Author: zouying
# @FileName: 977.有序数组的平方.py
# @Software: PyCharm

class Solution(object):
    # 非常烂的解法
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            nums[i] = nums[i] * nums[i]
        for i in range(0, len(nums)):
            for j in range(1, len(nums) - i):
                if nums[j] < nums[j-1]:
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp
        return nums
    # 归并算法
    def sortedSquares1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        NewNums = []
        flag = -1
        for i in range(0, len(nums)):
            if nums[i] < 0:
                flag = i
            nums[i] = nums[i] * nums[i]
        if flag == -1:
            return nums
        else:
            n = flag
            p = flag + 1
            i = 0
            while n >= 0 and p < len(nums):
                if nums[n] < nums[p]:
                    NewNums.append(nums[n])
                    n -= 1
                else:
                    NewNums.append(nums[p])
                    p += 1
                i += 1
            while i < len(nums) and n >= 0:
                NewNums.append(nums[n])
                n -= 1
                i += 1
            while i < len(nums) and p < len(nums):
                NewNums.append(nums[p])
                p += 1
                i += 1
        return NewNums
        # 双向指针
    def sortedSquares2(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            NewNums = [None]*len(nums)
            left = 0
            right = len(nums)-1
            i = len(nums) - 1
            while left <= right:#i>=0也对
                if nums[left] * nums[left] > nums[right] * nums[right]:
                    NewNums[i] = nums[left] * nums[left]
                    left += 1
                else:
                    NewNums[i] = nums[right] * nums[right]
                    right -= 1
                i -= 1
            return NewNums

if __name__ == '__main__':
    solution = Solution
    print(solution.sortedSquares2(solution, [-4,-1,0,3,10]))
    print(solution.sortedSquares2(solution, [-7, -3, 2, 3, 11]))
