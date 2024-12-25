"""1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.

Constraints:
------------
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

"""

class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:

