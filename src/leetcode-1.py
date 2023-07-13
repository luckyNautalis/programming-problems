# Problem 1: Two Sum

"""
Constraints

1) 2 <= nums.length <= 10^4
2) -10^9 <= nums[i] <= 10^9
3) -10^9 <= target <= 10^9
4) Only one valid answer exists

"""

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Using Dictionary Collect all the elements w/ indices.
        nums_dict = {}
        for n, num in enumerate(nums):
           nums_dict[num] = n

        # Iterate through the list & see if there is a key in the nums_dict
        # that adds to equal the target, then return, if so.
        for n, num in enumerate(nums):

            complement = target - num # Difference, num + complment = target
            # Check if complement is a key & if the index is not the same as n
            # as it can be the sum of the same values. If its not the sum of
            # the same value then this second condition is not important.
            if complement in nums_dict and nums_dict[complement]!=n:
                return [n,nums_dict[complement]]
