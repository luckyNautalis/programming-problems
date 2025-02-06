"""1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Constraints
-----------

1) 1 <= nums.length <= 10^5
2) nums[i] is either 0 or 1
"""


class Solution:

    def longestSubarray(self, nums: list[int]) -> int:
        """
        Sliding Window Approach
        -----------------------
        Use a sliding window to inch through the nums
        maintaining that there is never more than 1 zero within
        the window. Keep track of whether we have a zero within
        the window, if we encounter another, then we make sure to
        close the window in to maintain one zero only. We return
        the difference in the right end of the window and the left
        which cuts off one element, that is, it assumes a deletion.

        Steps
        -----
        (Simple Case)
        1. If nums is size one, then return 0, since we must delete an element.

        (Initialization)
        2. Initialize variables for the left and right of the window
           at position 0. While, make a zero count variable, if the right
           end (at position 0) is on a zero we count that there is a zero
           in our window. Lastly, initialize a max ones count variable to the
           value of the first element.


        (Iterate)
        3. Expand the right end of the window right: If the right end encouters a zero,
           then check if the we already have a zero in the window. If there is already a
           zero in the window, then move the left end right until we cut off the left-most
           zero in the widnow. If there was not already a zero in the window, then make
           the zero condition True and compute the max 1's. Otherwise, compute the max 1's.

        (Stop)
        4. Repeat the iteration of step (3) until the right end reaches the end of the array.
           Then return the max 1's.
        """
        if len(nums) == 1:
            return 0

        left = 0
        zero_cond = nums[0] == 0  # zero in window?
        max_ones = nums[0]

        for right in range(1, len(nums)):
            if nums[right] == 0:
                if zero_cond == True:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    max_ones = max(max_ones, right - left)
                    zero_cond = True
            else:
                max_ones = max(max_ones, right - left)
        return max_ones
