# -*- coding: utf-8 -*-            
# @Time : 2023/1/3 15:51
# @Author: zouying
# @FileName: 15. 三数之和.py
# @Software: PyCharm
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist = []
        nums.sort()
        if len(nums) < 3:
            return rlist
        for i in range(len(nums)-2):
            cur = nums[i]
            left = i+1
            right = len(nums)-1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if cur + nums[left] + nums[right] > 0:
                    right -= 1
                elif cur + nums[left] + nums[right] < 0:
                    left += 1
                elif cur + nums[left] + nums[right] == 0:
                    rlist.append([cur, nums[left], nums[right]])
                    while left < right and nums[right-1]==nums[right]:
                        right -= 1
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    right -= 1
                    left += 1

        return rlist
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        relist = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(len(nums)):
                    if i != j and j != k and i != k:
                        sum = nums[i]+nums[j]+nums[k]
                        if sum == 0:
                            r = [nums[i], nums[j], nums[k]]
                            r.sort()
                            if r not in relist:
                                relist.append(r)
        return relist
if __name__ == '__main__':
    solution = Solution
    print(solution.threeSum(solution, [-1,0,1,2,-1,-4]))