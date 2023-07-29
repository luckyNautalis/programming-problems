// Problem 674: Longest Continuous Increasing Subsequence

/**
 * Constraints:
 *
 * 1) 1 <= nums.length <= 10^4
 * 2) -10^9 <= nums[i] <= 10^9
 *
 */

class Solution {
    /**
     * A function that finds the length of the longest continuous increasing
     * subsequence within an int array.
     * @param nums The int array where LCIS is found.
     * @return LCIS The longest continuous increasing subsequence.
     */
    public int findLengthOfLCIS(int[] nums) {
        int CIS = 1, LCIS = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            // Lets count the number of continuous increases:
            // Each time we increse, increment and re-assign 'LCIS' to 'CIS'
            // if its 'CIS' > 'LCIS'.
            // Lets also see if there is a continuous decrease:
            // If there is we know the continuity of increases is broken and
            // we must assign 'CIS' to 1.
            if (nums[i] < nums[i+1]) {CIS++; LCIS = Math.max(LCIS, CIS);}
            else CIS = 1;
        }

        return LCIS;
    }
}
