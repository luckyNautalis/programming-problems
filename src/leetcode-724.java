/*
 * 724. Find Pivot Index
 * 
 * Given an array of integers nums, calculate the pivot index of this array.
 * 
 * The pivot index is the index where the sum of all the numbers strictly to the
 * left of the index is equal to the sum of all the numbers strictly to the
 * index's right.
 * 
 * If the index is on the left edge of the array, then the left sum is 0 because
 * there are no elements to the left. This also applies to the right edge of the
 * array.
 * 
 * Return the leftmost pivot index. If no such index exists, return -1.
 * 
 * Constraints
 * -----------
 * 
 * 1 <= nums.length <= 10^4
 * -1000 <= nums[i] <= 1000
 */
class Solution {

    public int pivotIndex(int[] nums) {

        /*
         * To get the left most pivot we get the total sum of nums.
         * Take a left sum by iterating over all elements after
         * the first in nums, where the current iteration represents the movement
         * of the left most pivot. Checking to see if double the left sum is equal to
         * the right sum, which is everything to the right of the left pivot, then
         * add the left pivot's value to the left sum. If, double theleft sum is
         * equivalent to the right sum (sum - nums[left pivot]), then return the left
         * pivot. Otherwise, at the iterations end there is no left most pivot, so
         * return -1.
         */
        int sum = 0;
        for (int n : nums)
            sum += n;

        int leftSum = 0;
        for (int leftPivot = 0; leftPivot < nums.length; leftPivot++) {
            if (leftSum * 2 == sum - nums[leftPivot])
                return leftPivot;
            leftSum += nums[leftPivot];
        }

        return -1;
    }
}
