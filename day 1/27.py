# -*- coding: utf-8 -*-            
# @Time : 2022/12/28 20:14
# @Author: zouying
# @FileName: 27.py
# @Software: PyCharm
class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while right >= 0 and nums[right] == val:
            right -= 1
            if right < 0:
                return left
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                nums[right] = val
                right -= 1
            left += 1
            while right >= 0 and nums[right] == val:
                right -= 1
            if right < 0:
                break
        return left
    # 暴力解法
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                for j in range(i+1,length):
                    nums[j-1] = nums[j]
                i -= 1
                length -= 1
            i += 1
        return length
    #快慢指针法
    def removeElement3(self, nums, val):
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
    #改进版双向指针
    def removeElement4(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[right] == val:
                right -= 1
            while left <= right and nums[left] != val:
                left += 1
            if left < right :
                nums[left] = nums[right]
                nums[right] =val
                left += 1
                right -= 1
        return left
if __name__ == '__main__':
    solution = Solution
    print(solution.removeElement2(solution, [3,2,2,3], 3))
    print(solution.removeElement2(solution, [0,1,2,2,3,0,4,2], 2))