"""1822. Sign of the Product of an Array

Implement a function signFunc(x) that returns:

1) 1 if x is positive.
2) -1 if x is negative.
3) 0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Constraints
-----------
1) 1 <= nums.length <= 1000
2) -100 <= nums[i] <= 100
"""


class Solution:

    def arraySign(self, nums: List[int]) -> int:

        def signFunc(x: int):
            if x < 0:
                return -1
            if x == 0:
                return 0
            return 1

        prod = 1
        for n in nums:
            prod *= n
            if n == 0:
                break
        return signFunc(prod)
