class LowerBound {
    /**
     * Given some number this function will determine the lower bound, that is,
     * the smallest index of a sorted int array where it is greater or equal
     * to the number provided.
     * @param array A sorted array of int.
     * @param target The lower bound is found in relation to the target.
     * @return low The lowest index greater or equal to the target.
     */
    public static int lowerBound(int[] nums, int target) {
        int low = 0, mid, high = nums.length - 1;
        while (low <= high) {
            mid = (low + high) / 2;
            if (nums[mid] >= target)
                high = mid - 1; // Search to the left of 'mid', index.
            else low = mid + 1; // Search to the right of 'mid', index.
        }
        if (low < nums.length && nums[low] < target)
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
