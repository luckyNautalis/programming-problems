/**
 * Problem 2180: Count Integers With Even Digit Sum
 *
 * Given a positive integer num, return the number of positive integers less
 * than or equal to num whose digit sums are even.
 *
 * The digit sum of a positive integer is the sum of all its digits.
 *
 * Constraints:
 * 
 * - (1 <= num <= 1000)
 */
class Solution {

    public int countEven(int num) {
        int evenCount = 0;
        String numStr;
        int sum = 0;
        while (num > 1) {
            numStr = Integer.toString(num);
            for (int i = 0; i < numStr.length(); i++) {
                sum += (int) numStr.charAt(i);
            }
            if (sum % 2 == 0)
                evenCount++;
            sum = 0;
            num--;
        }
        return evenCount;
    }
}
