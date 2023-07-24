// Problem 300: Longest Increasing Subsequence

/**
 * Constraints:
 *
 * 1) 1 <= nums.length <= 2500
 * 2) -10^4 <= nums[i] <= 10^4
 *
 */

import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    /**
     * This function finds the longest increasing subsequnce given an array
     * of type int.
     * @param nums The array where the longest increasing subsequence is found
     * @return temp.size() The size of the longest increasing subsequence
     */
    public int lengthOfLIS(int[] nums) {
        // We only want the first element of 'nums' in a ArrayList used to
        // represent the length of the longest increasing subsequence.
        // This will not always be the actual subsequence but close since its
        // elements may be replaced.
        ArrayList<Integer> temp = new ArrayList<>(Arrays.asList(nums[0]));
        for (int i = 1; i < nums.length; i++) {
            // If the ith element is greater than the (i-1)th element of nums
            // then we know we have an increase and we want to add this to our
            // LIS representation, 'temp'.
            if (nums[i] > temp.get(temp.size() - 1)) temp.add(nums[i]);
            // If the ith element is less than or equal to the (i-1)th element
            // of nums then we know we have either a decrease or the same number
            // as before. So, we want to replace the the first
            // number in 'temp' that is >= 'nums[i]' with 'nums[i]'.
            else {
                int replaceIndex = lowerBound(temp, nums[i]);
                temp.set(replaceIndex, nums[i]);
            }
        }

        return temp.size();
    }

    /**
     * Given some number this function will determine the lower bound, that is,
     * the smallest index of a sorted ArrayList such that it is greater or
     * equal to the number provided.
     * @param numList A sorted ArrayList to search through for the lower bound
     * @param target The lower bound is found with respect to the target number
     * @return low The lowest index greater or equal to target
     * */
    public static int lowerBound(ArrayList<Integer> numList, int target) {
        int low = 0, mid, high = numList.size() - 1;
        while (low < high) {
            mid = (low + high) / 2;
            // if the element at 'mid' is >= to the target then
            // we want to search to the left of 'mid'.
            if (numList.get(mid) >= target) {
                high = mid - 1;
            }
            // If the element at 'mid' is < than the 'target' then
            // we want to search to the right of 'mid'.
            else low = mid + 1;
        }
        // If the 'target' is greater than the last element of the
        // list then lower bound is not in the list.
        if (low < numList.size() && numList.get(low) < target) low++;

        return low;
    }
}
