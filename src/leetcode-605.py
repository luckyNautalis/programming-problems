#!/usr/bin/env python3
# Probelem 605: Can Place Flowers

"""
Constraints:

1) 1 <= flowerbed.length <= 2 * 104
2) flowerbed[i] is 0 or 1.
3) There are no two adjacent flowers in flowerbed.
4) 0 <= n <= flowerbed.length

"""
from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        0 is an empty plot and 1 is a non-empty plot, a flower cannot be planted if
        there is a plant adjacent to it. We want to see the max number of plants
        that are plantable. If max number is greater or equal to 'n', then we
        return true, else return false.
        """
        plantable: int = 0
        for p in range(len(flowerbed)):

            if flowerbed[p] == 0:
                empty_left = (p == 0) or (flowerbed[p - 1] == 0) # empty first place or empty between place
                empty_right = (p == len(flowerbed) - 1) or (flowerbed[p + 1] == 0) # empty last place or empty between place

                # Are both plots empty?
                if empty_left and empty_right:
                    flowerbed[p] = 1
                    plantable += 1

        return plantable >= n
