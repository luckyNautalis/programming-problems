// Problem 67: Add Binary

/**
 * Constraints:
 *
 * 1) 1 <= a.length, b.length <= 10^4
 * 2) a and b consist only of '0' or '1' characters
 * 3) Each string does not contain leading zeros except for the zero itself
 *
 */

import java.math.BigInteger;
import java.lang.Character;

class Solution {
    // Function to convert a String of Binary to String of decimal equivalent:
    public String binaryToDecimal(String s) {
        BigInteger decimal = BigInteger.ZERO;
        int power = -1; // Representing the power of 2. We can initialize power
                        // to first -1 we and add 1 for each iteration.
        for (int i = s.length() - 1; i >= 0; i--) {
           BigInteger num = BigInteger.valueOf(Character.getNumericValue(s.charAt(i)));
           power += 1;
           // If the power is base 2 power is 1 (2^power)^1:
          if (num.equals(BigInteger.ONE)) {
               num = BigInteger.TWO.pow(power);
           }
           decimal = decimal.add(num);
        }
        return decimal.toString();
    }
    // Fix This SHit
    public String decimalToBinary(String s) {

        BigInteger sBigInt = new BigInteger(s);
        String revBin = ""; // To be reversed...
        if (s.equals("0")) {
                return "0";
            }
        else {
            while (sBigInt.compareTo(BigInteger.ZERO) > 0) {
                if (sBigInt.remainder(BigInteger.TWO).equals(BigInteger.ONE)) {
                    revBin += '1';
                }
                else {
                    revBin += '0';
                }
                sBigInt = sBigInt.divide(BigInteger.TWO);
            }
            String bin = "";
            for (int i = revBin.length() - 1; i >= 0; i--) {
                bin += revBin.charAt(i);
            }
        return bin;
        }
    }
    public String addBinary(String a, String b) {

        BigInteger aBigInt = new BigInteger(binaryToDecimal(a));
        BigInteger bBigInt = new BigInteger(binaryToDecimal(b));
        BigInteger sumBigInt = aBigInt.add(bBigInt);
        String decimalSumStr = sumBigInt.toString();
        return decimalToBinary(decimalSumStr);
    }
}
