"""88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints
-----------
1) nums1.length == m + n
2) nums2.length == n
3) 0 <= m, n <= 200
4) 1 <= m + n <= 200
4) -10^9 <= nums1[i], nums2[j] <= 10^9
"""


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1
        while j >= 0:
            nums1[i + j + 1] = nums2[j]
            j -= 1
