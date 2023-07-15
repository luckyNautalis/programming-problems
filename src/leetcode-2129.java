// 2129. Capitlize the Title

/**
 * Constraints:
 *
 * 1) 1 <= title.length <= 100
 * 2) title consists of words separated by a single space without any leading or trailing spaces.
 * 3) Each word consists of uppercase and lowercase English letters and is non-empty.
 *
 */

class Solution {

    public String capitalizeTitle(String title) {

        char[] charArr = title.toCharArray();
        int titleLen = title.length();

        // Convert each to lower for easy operation
        for (int i = 0; i < titleLen; i++)
            charArr[i] = Character.toLowerCase(charArr[i]);

        // Now we can go the first to last character of each word
        int first = 0;
        for (int last = 0; last < titleLen; last++) {

            first = last;
            while (last < titleLen && !Character.isWhitespace(charArr[last]))
                last++;

            if (last - first > 2)
                charArr[first] = Character.toUpperCase(charArr[first]);
        }
        return String.valueOf(charArr);
    }
}
