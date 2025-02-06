
/*
 * 66. Plus One
 *
 * You are given a large integer represented as an integer array digits, where
 * each digits[i] is the ith digit of the integer. The digits are ordered from
 * most significant to least significant in left-to-right order. The large
 * integer does not contain any leading 0's.
 *
 * Increment the large integer by one and return the resulting array of digits.
 *
 * Constraints
 * -----------
 * 1) 1 <= digits.length <= 100
 * 2) 0 <= digits[i] <= 9
 * 3) digits does not contain any leading 0's.
 *
 */
class Solution {

    public int[] plusOne(int[] digits) {
        /*
         * This question just wants you to add 1
         * and carry it over if you need to.
         *
         * (Iterate)
         * 1. From last to first digit:
         * If the digit is not 9, increment it and return the array.
         * If it is 9, set it to 0 and continue to the next digit.
         * 
         * 2. If we've gone through all digits without returning,
         * it means all digits were 9. In this case, create a new array
         * with an additional digit, set the first digit to 1, and return it.
         */
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}
