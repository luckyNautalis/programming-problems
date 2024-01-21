#!/usr/bin/env python3
# Problem 334: Increasing Triplet Sequence
from typing import List

class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        """ Find two increasing, then one more, in order."""
        if len(nums) < 3: return False
        i = j = float('inf') # Initial out of range points for low and mid points.
        for k in nums:
            # If k = i, then we can change the ith place since we know j is greater.
            # If k < i, then we can change the ith place and search k > j.
            if k <= i:
                i = k
            # If k <= j, then j becomes a mid-point and we look for a k greater than j.
            elif k <= j:
                j = k
           # Then, we have a nums[i] < nums[j] < nums[k] where i < j < k.
            else:
                return True

        # There are no increasing triplets.
        return False
