# Problem 628: Maximum Product of Three Numbers

"""
Constraints:

1) 3 <= nums.length <= 10^4
2) -1000 <= nums[i] <= 1000

"""

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """
        Find the maximum product of three integers from the given list.

        This method takes a list of integers as input and returns the maximum product
        that can be obtained by multiplying three integers from the list.

        Parameters:
            self (Solution): The current instance of the Solution class.
            nums (list[int]): A list of integers from which to find the maximum product.

        Returns:
            int: The maximum product of three integers from the given list.
        """
        nums.sort()
        n : int = len(nums) - 1
        return max(nums[0]*nums[1]*nums[-1], nums[n-2]*nums[n-1]*nums[n])
