#!/usr/bin/env python3
# Probelem 238: Product of Array Except Self
"""
Constraints:

1) 2 <= nums.length <= 105
2) -30 <= nums[i] <= 30
3) The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
4) Solution must be O(n)
"""
from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer: List[int] = []
        n = len(nums)
        # Initialize two arrays to store the left prodcuts (from left of n[i])
        # and to store the right products (from the right of n[i]).
        left_products = [1] * n
        right_products = [1] * n

        # Calculate each prodcut from the left of nums[i] and store in left_products.
        left_product: int = 1
        for i in range(1, n):
           left_product *= nums[i - 1]
           left_products[i] = left_product

        # Calculate each product from the right of nums[i] and store in right_products.
        right_product: int = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product

        # Get prodcucts except self by multiply the the left prodcut and right prodcuct for each
        # index.
        answer = [left_products[i] * right_products[i] for i in range(n)]
        return answer
