"""643. Maximum Average Subarray 1

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error
less than 10-5 will be accepted.

Constraints
-----------
- n == nums.length
- 1 <= k <= n <= 10^5
- -(10^4) <= nums[i] <= 10^4
"""


class Solution:

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_total = total = sum(nums[:k])
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            max_total = max(total, max_total)
        return max_total / k
