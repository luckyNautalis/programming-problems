"""896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Constraints
-----------
1) 1 <= nums.length <= 10^5
2) -10^5 <= nums[i] <= 10^5
"""


class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:
        step = 1
        start, stop = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            step = -1
            start, stop = stop, start

        for i in range(start, stop, step):
            if nums[i] > nums[i + step]:
                return False

        return True
