#!/usr/bin/env python3
# Problem 1431: Kids With the Greatest Number of Candies

"""
Constraints:

1) n == candies.length
2) 2 <= n <= 100
3) 1 <= candies[i] <= 100
4) 1 <= extraCandies <= 50

"""
from typing import List

class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        kids_greatest_candies: List[bool] = []
        max_candies: int = max(candies)

        for k in candies:

            if (k + extraCandies) < max_candies:
                kids_greatest_candies.append(False)
            else:
                kids_greatest_candies.append(True)

        return kids_greatest_candies
