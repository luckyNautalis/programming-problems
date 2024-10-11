
/**
 * Problem 912: Sort An Array
 *
 * Given an array of integers nums, sort the array in ascending order and return
 * it.
 * 
 * You must solve the problem without using any built-in functions in O(nlog(n))
 * time complexity and with the smallest space complexity possible.
 *
 * Constraints:
 * - 1 <= nums.length <= 5 * 10^4
 * - (-5) * 10^4 <= nums[i] <= 5 * 10^4
 */
import java.util.Arrays;

class Solution {
    /**
     * Solving using merge sort algo.
     *
     * @param nums Non-emtpy array of numbers.
     * @return Sorted `nums` array of numbers.
     */
    public int[] sortArray(int[] nums) {
        if (nums.length == 1)
            return nums;

        // Split array in half
        int mid = nums.length / 2;
        int[] l = Arrays.copyOfRange(nums, 0, mid);
        int[] r = Arrays.copyOfRange(nums, mid, nums.length);

        // Keep on splitting till length 1
        l = sortArray(l);
        r = sortArray(r);

        // Merge & sort component arrays
        return merge(l, r);
    }

    /**
     * Merges and sorts two arrays into one.
     *
     * @param l Array to be merged.
     * @param r Array to be merged.
     * @return Sorted and merged array.
     */
    public int[] merge(int[] l, int[] r) {
        int[] merged = new int[l.length + r.length];
        int i = 0;
        int j = 0;

        while (i < l.length && j < r.length)
            merged[i + j] = (l[i] <= r[j]) ? l[i++] : r[j++];
        while (i < l.length)
            merged[i + j] = l[i++];
        while (j < r.length)
            merged[i + j] = r[j++];

        return merged;
    }
}
