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

// Iterating & Using Binary Search.
class Solution {
    /**
     * This function finds the longest increasing subsequnce given an array
     * of type int.
     * @param nums The array where the longest increasing subsequence is found
     * @return temp.size() The size of the longest increasing subsequence
     */
    public int lengthOfLIS(int[] nums) {
        // We can just initialize the ArrayList 'temp' with the first element
        // of 'nums' it will be the starting point. The length starts at 1
        // and from here we can test if we increase.
        ArrayList<Integer> temp = new ArrayList<>(Arrays.asList(nums[0]));
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > temp.get(temp.size() - 1))
                // If the next element after the latest within 'temp' is greater
                // then we want to add that to 'temp', to get a longer subsequence.
                temp.add(nums[i]);
            else {
                // If the next element of 'nums' is less than or equal to the last
                // element of 'temp' then were presented with either a smaller
                // number or the same number as before. In this case, we want to
                // replace the smallest number that is greater or equal to 'nums[i]'
                // with 'nums[i]' the smaller number. In, effect we are leaving
                // the length of 'temp' unchanged so we may continue searching for
                // actual increments.
                int replaceIndex = lowerBound(temp, nums[i]);
                temp.set(replaceIndex, nums[i]);
            }
        }

        return temp.size();
    }

    /**
     * Given some number this function will determine the lower bound, that is,
     * the smallest index of a sorted ArrayList where it is greater or
     * equal to the number provided.
     * @param numList A sorted ArrayList to search through for the lower bound
     * @param target The lower bound is found with respect to the target number
     * @return low The lowest index greater or equal to target
     * */
    public static int lowerBound(ArrayList<Integer> numList, int target) {
        int low = 0, mid, high = numList.size() - 1;
        while (low < high) {
            mid = (low + high) / 2;
            if (numList.get(mid) >= target)
                high = mid - 1; // Search to the left of 'mid', index.
            else low = mid + 1; // Search to the right of 'mid', index.
        }
        if (low < numList.size() && numList.get(low) < target)
            // If the current lower bound, 'low' is less than the size of the
            // list 'numsList' then we know the lower bound is not already the
            // last index/element of the 'numList'.
            // While, If the 'target' is greater than the last element of the
            // list then lower bound is not in the list and we must increment to
            // make the lower bound the last index/element of 'numList'.
            low++;

        return low;
    }
}
