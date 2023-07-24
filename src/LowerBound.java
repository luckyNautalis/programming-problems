class LowerBound {
    // Find the index of the element that is the smallest next to the target.
    public static int lowerBound(int[] array, int target) {
        int low = 0, mid, high = array.length - 1;
        while (low <= high) {
            mid = (low + high) / 2;
            if (array[mid] >= target) high = mid - 1;
            else low = mid + 1;
        }
        if (low < array.length && array[low] < target) low++;

        return low;
    }

    public static void main(String[] args) {

        int[] nums = {1,2,3,4,5,6,8,33,44,47,77};
        System.out.println(lowerBound(nums, 88));
    }
}
