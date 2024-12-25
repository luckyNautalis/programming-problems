/**
 * Problem 4: Median of Two Sorted Arrays
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return
 * the median of the two sorted arrays.
 * 
 * The overall run time complexity should be O(log (m+n)).
 *
 * Constraints:
 * - nums1.length == m
 * - nums2.length == n
 * - 0 <= m <= 1000
 * - 0 <= n <= 1000
 * - 1 <= m + n <= 2000
 * - (-10^6) <= nums1[i], nums2[i] <= 10^6
 */
class Solution {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length == 0) {
            double median = nums2[nums2.length / 2];
            if (nums2.length % 2 == 0)
                median = (nums2[nums2.length / 2 - 1] + median) / 2;
            return median;
        }
        if (nums2.length == 0) {
            double median = nums1[nums1.length / 2];
            if (nums1.length % 2 == 0)
                median = (nums1[nums1.length / 2 - 1] + median) / 2;
            return median;
        }

        int upBound = nums1.length + nums2.length;
        int[] nums = new int[upBound / 2 + 1];
        int i = 0;
        int j = 0;

        while (i + j < nums.length) {
            if (i < nums1.length && j < nums2.length)
                nums[i + j] = (nums1[i] < nums2[j]) ? nums1[i++] : nums2[j++];
            else if (i < nums1.length)
                nums[i + j] = nums1[i++];
            else
                nums[i + j] = nums2[j++];
        }

        double median = nums[upBound / 2];
        if (upBound % 2 == 0)
            median = (nums[upBound / 2 - 1] + median) / 2;

        return median;
    }
}
