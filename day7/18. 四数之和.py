# -*- coding: utf-8 -*-            
# @Time : 2023/1/3 22:35
# @Author: zouying
# @FileName: 18. 四数之和.py
# @Software: PyCharm
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rlist = []
        nums.sort()
        if len(nums) < 4:
            return rlist
        for k in range(len(nums)):
            if k>0 and nums[k] == nums[k-1]:
                continue
            for i in range(k+1, len(nums)):
                cur = nums[i]
                left = i + 1
                right = len(nums) - 1
                if i > k+1 and nums[i] == nums[i - 1]:
                    continue
                while left < right:
                    if nums[k]+cur + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[k]+cur + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[k]+cur + nums[left] + nums[right] == target:
                        rlist.append([nums[k], cur, nums[left], nums[right]])
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        right -= 1
                        left += 1
        return rlist
if __name__ == '__main__':
    solution = Solution
    print(solution.fourSum(solution, [1,0,-1,0,-2,2], target = 0))