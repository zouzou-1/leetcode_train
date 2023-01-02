# -*- coding: utf-8 -*-            
# @Time : 2023/1/2 15:15
# @Author: zouying
# @FileName: 1. 两数之和.py
# @Software: PyCharm
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i in range(0, len(nums)):
            if target-nums[i] in record.keys():
                return [record[target-nums[i]], i]
            record[nums[i]] = i

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i]+nums[j]==target:
                    return [i, j]




if __name__ == '__main__':
    solution = Solution
    print(solution.twoSum(solution,  [2,7,11,15], 9))