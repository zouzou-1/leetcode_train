# -*- coding: utf-8 -*-            
# @Time : 2022/12/28 19:02
# @Author: zouying
# @FileName: 704.py
# @Software: PyCharm



class Solution(object):
    # 左闭右开
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        left = 0
        right = len(nums)
        while (left < right):
            middle = int((left + right) / 2)
            if nums[middle] == target:
                index = middle
                break
            elif nums[middle] > target:
                right = middle
            else:
                left = middle + 1
        print(index)

    # 左闭右闭
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        left = 0
        right = len(nums)-1
        while (left <= right):
            middle = int((left + right) / 2)
            if nums[middle] == target:
                index = middle
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        print(index)

if __name__ == '__main__':
    solution = Solution
    solution.search2(solution, [-1, 0, 3, 5, 9, 12], 9)
    solution.search2(solution, [-1, 0, 3, 5, 9, 12], 2)
