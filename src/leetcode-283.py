# Problem 283: Move Zeros
"""
Constraints:

1) 1 <= nums.length <= 104
2) -231 <= nums[i] <= 231 - 1
"""
from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Using two pointers, we organize all non-zero elements at the start of nums by checking each
        index of nums for non-zero elements. If there is a non-zero element at some index,
        then assign that element to nums[non_zero]. The pointer non_zero will either be at the start
        of nums or right after the last occurrence of a non-zero element because we move this pointer
        up one whenever we find a non-zero element (so that it points to the element at the next "non-zero"),
        while also assigning the current element of the iteration to the element at the next "non-zero."
        """
        non_zero: int = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[non_zero], nums[n] = nums[n], nums[non_zero]
                non_zero += 1
