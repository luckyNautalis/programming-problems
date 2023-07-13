# 1493. Longest Subarray of 1's After Deleting One Element




class Solution:

    def longestSubarray(self, bit_array: list[int]) -> int:
        """
        Given a binary array 'bit_array', you should delete one element from it.

        Return the size of the longest non-empty subarray containing only 1's in
        the resulting array. Return 0 if there is no such subarray.
        """

        """ To get the longest subarray of 1's after deleting one element:

            1. We must find the max length of the subarray of 1's:

               - We can do so by considering two subarrays, the
                 'left_subarray_length' and the 'right_subarray_length' that
                 capture the 1's on to the left and right, respectively. Both
                 'left_subarray_length' and 'right_subarray_length' sum to
                 'subarray_length'.

               - We then can get the longest subarray of 1's, 'max_ones' by
                 checking each iteration if the 'subarray_length' is greater
                 than the current 'max_ones'. If so then update 'max_ones' to
                 'subarray_length'.

            2. To find when 'subarray_length' we will use boundaries:

               - Lets use two bounds, 'left_bound' and 'right_bound'.


        """

# [1,1,0,1]
