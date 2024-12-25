"""1679. Max Number of K-sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose
sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Constraints
-----------
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    - 1 <= k <= 10^9
"""


class Solution:

    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            n = nums[l] + nums[r]
            if n == k:
                l += 1
                r -= 1
                count += 1
            elif n < k:
                l += 1
            else:
                r -= 1
        return count
