// Problem 673: Number of Longest Increasing Subsequence

/**
 * Constraints:
 *
 * 1) 1 <= nums.length <= 2000
 * 2) -10^6 <= nums[i] <= 10^6
 *
 */
import java.util.Arrays;

class Solution {
    /**
     * This function find the number of LIS given an int array.
     * @param nums The array to find the number of LIS
     * @return numLIS The number of LIS.
     */
    public int findNumberOfLIS(int[] nums) {
        int LIS = 1; // Longest length is at least 1.
        // We want to keep track of the lengths to find the LIS and we want to
        // keep track of the count of LIS.
        int[] lengths = new int[nums.length], counts = new int[nums.length];
        // The 'lengths' and the 'counts' will be at least 1.
        Arrays.fill(lengths, 1); Arrays.fill(counts, 1);

        for (int i = 0; i < nums.length; i++) {
            // We will find the lengths of increasing subsequences from
            // 'nums[j]' to 'nums[i]'. While, update the counts of the
            // longest increasing subsequence.
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i] && lengths[j] + 1 > lengths[i]) {
                    // If the element 'i' is an increase from one of the
                    // previous elements at 'j', and one of the previous lengths
                    // plus 1 (for the current greater element)
                    // is greater than the current length at 'i', then
                    // we can assign the current length to the previous length
                    // plus 1.
                    lengths[i] = lengths[j] + 1; 
                    // Since this is the first time the length increased we
                    // must assign the count at 'i' to the count at 'j'. This
                    // will make sure that count of 'LIS' is the same as the
                    // count of all the different counts of the last
                    // longest increasing subsequnce at 'j' but plus 1 for the
                    // element at 'i'.
                    counts[i] = counts[j];
                }
                else if (nums[j] < nums[i] && lengths[j] + 1 == lengths[i]) {
                    // When we see that the length of the last longest
                    // increasing subsequence plus 1 (for the element 'i') is
                    // the same as the length at 'i' and there is an increase
                    // from 'nums[j]' to 'nums[i]'. Then the count should
                    // increase by the count at 'j' so that the count gets
                    // all of the different length combinations at 'j'.
                    //
                    counts[i] += counts[j];
                }
            }
            LIS = Math.max(LIS, lengths[i]); // Update to longest
        }
        int numLIS = 0;
        // Here we to first check if 'LIS' is 1, if it is, then we know
        // that the number of length 1's is the same as the length of the array.
        // If not, we will just want to go through the array of lengths and
        // increment the 'numLIS' each time we see a multiple we will add the
        // count at that point to 'numLIS'.
        if (LIS == 1) numLIS = nums.length;
        else
            for (int dup = 0; dup < lengths.length; dup++)
                 if (LIS == lengths[dup]) numLIS += counts[dup];

        return numLIS;
    }
}
