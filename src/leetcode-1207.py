"""1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Constraints
-----------
1) 1 <= arr.length <= 1000
2) -1000 <= arr[i] <= 1000
"""


class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Checks if the number of unique elements is equal to the
        # number of unique element counts.
        return len({*arr}) == len({*Counter(arr).values()})
