#!/usr/bin/env python3
# Problem 11: Container With The Most Water
"""
Constraints:

1) n == height.length
2) 2 <= n <= 10^5
3) 0 <= height[i] <= 10^4
"""
from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:
        """
        To get the max area we use two pointers at each end of the list.
        We get the areas of sections from a left pointer (i) and right pointer
        (j), getting the width of the section the absolute difference between
        the two and multiplying by the minimum height between the two pointers
        which act as bounds to hold the water.

        The important step is to know whether to shift the left or right, that is, whether
        to shift the left pointer (i) right or to shift the right pointer (j) left. We want to
        shift to the bound that has the shortest height because we cannot hold water above that
        height if we shift the other bound, then we would not be able to increase our area of water held.

        Once, we make that shift we can calculate a new area that may be the max area if greater than the
        current max area. While, once we have shifted enough times we will have both bounds equal or an area of
        0 which is when we know that we cannot increase our areas any longer.

        An optimization to this is to break out of iteration if the max area is greater than the maximum
        possible area from the current width (from our current bounds) multiplied by the maximum of the heights.
        Note: This may not be a realistic area, but it tells us that we cannot get a larger area by manipulating
        the bounds anymore.
        """
        i: int = 0
        j: int = len(height) - 1
        max_height: int = max(height)
        next_area: int = 0
        max_area: int = 0
        while i != j:
            next_area = (j-i) * min(height[j], height[i])
            max_area = max(next_area, max_area)
            if max_area >= (j-i) * max_height:
                break
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return max_area
