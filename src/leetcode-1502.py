"""1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


Constraints
-----------
1) 2 <= arr.length <= 1000
2) -10^6 <= arr[i] <= 10^6
"""


class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        prog = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != prog:
                return False
        return True
