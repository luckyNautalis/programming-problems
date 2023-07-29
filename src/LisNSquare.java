// For leetcode problem 300 and 673.

/**
 * Constraints:
 *
 * 1) 1 <= nums.length <= 2500
 * 2) -10^4 <= nums[i] <= 10^4
 *
 */

import java.util.Arrays;

class LisNSquare {
    /**
     * A function that will get the length of the longest increasing subsequence
     * of an int array.
     * @param nums Where the length longest increasing subsequence is found.
     * @return lis The length of the lonest increasing subsequence.
     */
    public int lengthOfLIS(int[] nums) {
        int lis = 1; // Longest length is at least 1.
        int[] lengths = new int[nums.length];
        Arrays.fill(lengths, 1); // All lengths are at least 1.

        // We will find the length of some increasing subsequence from
        // 'nums[i]' to 'nums[j]'.
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i] && lengths[j] + 1 > lengths[i])
                    // If the next element is an increase from one of the
                    // previous elements, and one of the previous lengths
                    // plus 1 (for the current greater element)
                    // is greater than the current length at 'i', then
                    // we can assign the current length to the previous length
                    // plus 1.
                    lengths[i] = lengths[j] + 1;
            lis = Math.max(lis, lengths[i]); // Update lis to be max.
            }
        }

        return lis;
    }
}
