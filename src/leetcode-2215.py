"""2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Constraints
-----------
1) 1 <= nums1.length, nums2.length <= 1000
2) -1000 <= nums1[i], nums2[i] <= 1000
"""


class Solution:

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]
        set1, set2 = set(nums1), set(nums2)
        for n in set1:
            if n not in set2:
                result[0].append(n)
        for n in set2:
            if n not in set1:
                result[1].append(n)
        return result
