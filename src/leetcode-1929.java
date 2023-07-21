// Problem 1929: Concatenation of Array

/**
 * Constraints:
 *
 * 1) n == nums.length
 * 2) 1 <= n <= 1000
 * 3) 1 <= nums[i] <= 1000
 *
 */

class Solution {
    public int[] getConcatenation(int[] nums) {
        int ans[] = new int[2 * nums.length], start = 0, mid = nums.length;
        do {ans[start] = nums[start]; ans[mid] = nums[start]; start++; mid++;}
        while (start < nums.length);

        return ans;
    }
}
