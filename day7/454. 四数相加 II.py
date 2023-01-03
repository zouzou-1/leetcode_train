# -*- coding: utf-8 -*-            
# @Time : 2023/1/3 13:47
# @Author: zouying
# @FileName: 454. 四数相加 II.py
# @Software: PyCharm
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        record1 = {}
        for index, val in enumerate(nums1):
            if val in record1.keys():
                record1[val].append(index)
            else:
                record1[val] = [index]
        record2 = {}
        for index, val in enumerate(nums2):
            if val in record2.keys():
                record2[val].append(index)
            else:
                record2[val] = [index]
        record3 = {}
        for index, val in enumerate(nums3):
            if val in record3.keys():
                record3[val].append(index)
            else:
                record3[val] = [index]
        record4 = {}
        for index, val in enumerate(nums4):
            if val in record4.keys():
                record4[val].append(index)
            else:
                record4[val] = [index]
        sum_record12 = {}
        sum_record34 = {}
        for i in record1.keys():
            for j in record2.keys():
                sum12 = i + j
                if sum12 in sum_record12.keys():
                    sum_record12[sum12] += len(record1[i]) * len(record2[j])
                else:
                    sum_record12[sum12] = len(record1[i]) * len(record2[j])
        for x in record3.keys():
            for y in record4.keys():
                sum34 = x + y
                if sum34 in sum_record34.keys():
                    sum_record34[sum34] += len(record3[x]) * len(record4[y])
                else:
                    sum_record34[sum34] = len(record3[x]) * len(record4[y])
        sum = 0
        for i in sum_record12.keys():
            j = 0 - i
            if j in sum_record34.keys():
                sum += (sum_record12[i] * sum_record34[j])

        return sum
    # def fourSumCount1(self, nums1, nums2, nums3, nums4):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :type nums3: List[int]
    #     :type nums4: List[int]
    #     :rtype: int
    #     """
    #     sum = 0
    #     n = len(nums1)
    #     for i in nums1:
    #         for j in nums2:
    #             for x in nums3:
    #                 for y in nums4:
    #                     if i+j+x+y == 0:
    #                         sum += 1
    #     return sum
if __name__ == '__main__':
    nums1 = [-1, -1]
    nums2 = [-1, 1]
    nums3 = [-1, 1]
    nums4 = [1, -1]
    solution = Solution
    print(solution.fourSumCount(solution, nums1, nums2, nums3, nums4))