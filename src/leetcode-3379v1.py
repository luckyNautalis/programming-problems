"""3379. Transformed Array
You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:
For each index i (where 0 <= i < nums.length), perform the following independent actions:

    If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
    If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
    If nums[i] == 0: Set result[i] to nums[i].

Return the new array result.

Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

Constraints
-----------
1) 1 <= nums.length <= 100
2) -100 <= nums[i] <= 100
"""


class Solution:

    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        """
        Algorithmic Paradigm: Imperative
        Programming Paradigm: Iterative
        Complexity:
            - Time: O(n)
            - Space: O(n)
        """
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] > 0:
                result[i] = nums[(i + nums[i]) % n]
            elif nums[i] < 0:
                result[i] = nums[(i - abs(nums[i])) % n]
            else:
                result[i] = nums[i]

        return result


s = Solution()
nums = [-1, 4, -1]
print(s.constructTransformedArray(nums))
