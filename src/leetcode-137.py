# Problem 137: Single Number II

"""
Constraints:

1) 1 <= nums.length <= 3 * 10^4
2) -2^{31} <= nums[i] <= 2^{31} - 1
3) Each element in nums appears exactly three times except for one element which appears once

"""

class Solution:

    def singleNumber(self, nums: list[int]) -> int:

        if len(nums) > 1:

            for i in range(len(nums)):

                complement = nums[:]; del complement[i]
                if nums[i] not in complement:
                    return nums[i]
        else:
            return nums[0]

nums = [0,1,0,1,0,1,99]; s = Solution()
print(s.singleNumber(nums))
