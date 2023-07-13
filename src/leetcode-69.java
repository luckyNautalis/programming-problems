// Problem 69: Sqrt(x)

/**
 * Constraints:
 *
 * 1) 0 <= x <= 2^{31} - 1
 *
 */

class Solution {

    public int mySqrt(int x) {

        long max = x;
        long min = 0;
        long root = x;
        while (min<=max) {
            long mid = (max+min)/2;
            if (mid*mid==x) {
                return (int)mid;
            }
            else if (mid*mid<x) {
                min = mid + 1;
                root = mid;
            }
            else {
                max = mid - 1;
            }
        }
        return (int)root;
    }
}
