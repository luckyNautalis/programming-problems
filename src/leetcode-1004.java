/* 1004. Max Consecutive Ones III
 *
 * Given a binary array nums and an integer k, return the maximum number of
 * consecutive 1's in the array if you can flip at most k 0's.
 *
 * Constraints
 * -----------
 * - 1 <= nums.length <= 10^5
 * - nums[i] is either 0 or 1.
 * - 0 <= k <= nums.length
 *
 */

class Solution {

    public int longestOnes(int[] nums, int k) {
        /*
         * Sliding window
         *
         * Use a sliding window to count the maximum consecutive 1's.
         * If we encounter a 0 on the way, then we will count it as flipped
         * (not modifying), as long as our flip count < k. If flip count == k,
         * then we jump to the left end to the right of next 0.
         *
         * 1. (Simple Case)
         * If length of nums is 1 return 1.
         *
         * 2. (Initial)
         * Define a max ones, flip count (for 0's flipped 1), and left and right ends
         * of the sliding window.
         *
         * 3. (Iterative)
         * While we can move right, move the right end right. If there is 1
         * count it, if not count it as 1 only if we flip count < k, and make sure to
         * check for a max 1's. If flip count == k, then maintain the flip count by
         * moving the left end rigt until we subtract 0 (in this way we
         */
        if (nums.length == 1)
            return 1;

        int maxOnes = 0;
        int ones = 0; // temp count
        int flipCount = 0;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 1) {
                ones++;
                maxOnes = Math.max(ones, maxOnes);
            } else if (flipCount < k) {
                ones++;
                flipCount++;
                maxOnes = Math.max(ones, maxOnes);
            } else { // Maintain flip count = k
                while (nums[left] != 0) {
                    left++;
                    ones--;
                }
                left++;
            }
        }

        return maxOnes;
    }
}
