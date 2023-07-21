// Problem 1704: Determine if String Halves Are Alike


/**
 * Constraints:
 *
 * 1) 2 <= s.length <= 1000
 * 2) s.length is even.
 * 3) s consists of uppercase and lowercase letters.
 *
 **/

class Solution {
    public boolean halvesAreAlike(String s) {
        s = s.toLowerCase();
        int aVowelCount = 0, bVowelCount = 0;
        int start = 0, mid = s.length()/2;
        do {
            char startChar = s.charAt(start), midChar = s.charAt(mid);
            if (startChar == 'a' || startChar == 'e' || startChar == 'i'
                || startChar == 'o' || startChar == 'u') aVowelCount++;
            if (midChar == 'a' || midChar == 'e' || midChar == 'i'
                || midChar == 'o' || midChar == 'u') bVowelCount++;
            start++; mid++;
        } while (start < s.length()/2);

        return aVowelCount == bVowelCount;
    }
}
