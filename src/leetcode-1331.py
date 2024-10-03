""" Problem 1331: Rank Transform of an Array

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:
    - Rank is an integer starting from 1.
    - The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    - Rank should be as small as possible.

Constraints:
    - 0 <= arr.length <= 10^5
    - (-10^9) <= arr[i] <= 10^9
"""


def arrayRankTransform(self, arr: List[int]) -> List[int]:
    # Creates a mapping: numbers -> rank
    rank_map = {num: rank for rank, num in enumerate(sorted(set(arr)), start=1)}
    return [rank_map[num] for num in arr]
