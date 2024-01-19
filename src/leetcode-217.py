# Problem 217: Contains Duplicate

"""
Constraints:

1) 1 <= nums.length <= 10^5
2) -10^9 <= nums[i] <= 10^9

"""

from typing import List

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        has_duplicate : bool = False
        nums_set : set = set(nums)

        if len(nums) > len(nums_set):
            has_duplicate = True

        return has_duplicate
