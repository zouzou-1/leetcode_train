# -*- coding: utf-8 -*-            
# @Time : 2023/1/2 11:22
# @Author: zouying
# @FileName: 349. 两个数组的交集.py
# @Software: PyCharm
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rnums = []
        nums1_dict = {}
        for i in nums1:
            nums1_dict[i] = 1
        for j in nums2:
            if j in nums1_dict.keys() and nums1_dict[j] == 1:
                rnums.append(j)
                nums1_dict[j] = 0
        return rnums


    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_hashtable = [0]*1001
        nums2_hashtable = [0]*1001
        rnums = []
        for i in nums1:
            if nums1_hashtable[i] == 0:
                nums1_hashtable[i] = 1
        for j in nums2:
            if nums2_hashtable[j] == 0:
                nums2_hashtable[j] = 1
        index = 0
        for i,j in zip(nums1_hashtable, nums2_hashtable):
            if i == 1 and j == 1:
                rnums.append(index)
            index += 1

        return rnums




if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution
    print(solution.intersection(solution, nums1, nums2))