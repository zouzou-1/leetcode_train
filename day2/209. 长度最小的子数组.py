# -*- coding: utf-8 -*-            
# @Time : 2022/12/29 13:38
# @Author: zouying
# @FileName: 209. 长度最小的子数组.py
# @Software: PyCharm
class Solution(object):
    # 暴力算法
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        MinLen = len(nums) + 1
        for i in range(0, len(nums)):
            sum = 0
            for j in range (i, len(nums)):
                sum += nums[j]
                if sum >= target:
                    if MinLen > j-i+1:
                        MinLen = j-i+1
                    break
        if MinLen == len(nums) + 1:
            return 0
        return MinLen

        # 滑动窗口
    def minSubArrayLen2(self, target, nums):
            """
            :type target: int
            :type nums: List[int]
            :rtype: int
            """
            MinLen = len(nums) + 1
            begin = 0
            end = 0
            sum = 0
            while end < len(nums):
                sum += nums[end]
                if sum >= target:
                    if MinLen > end - begin + 1:
                        MinLen = end - begin + 1
                    sum -= nums[begin]
                    begin += 1
                    sum -= nums[end]
                    end -= 1
                end += 1
            if MinLen == len(nums) + 1:
                return 0
            return MinLen
    def minSubArrayLen3(self, target, nums):
            """
            :type target: int
            :type nums: List[int]
            :rtype: int
            """
            MinLen = len(nums) + 1
            begin = 0
            end = 0
            sum = 0
            while end < len(nums):
                sum += nums[end]
                while sum >= target:
                    if MinLen > end - begin + 1:
                        MinLen = end - begin + 1
                    sum -= nums[begin]
                    begin += 1
                end += 1
            if MinLen == len(nums) + 1:
                return 0
            return MinLen
if __name__ == '__main__':
    solution = Solution
    print(solution.minSubArrayLen3(solution, 7, [2,3,1,2,4,3]))
    print(solution.minSubArrayLen3(solution, 4, [1,4,4]))
    print(solution.minSubArrayLen3(solution, 11, [1,1,1,1,1,1,1,1]))
