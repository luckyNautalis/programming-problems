// Problem 2129: Capitlize the Title

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
    char[] chars = title.toLowerCase().toCharArray();
    int length = title.length();

    for (int start, end = 0; end < length; end++) {
      start = end;
      while (end < length && !Character.isWhitespace(chars[end])) end++;
      if (end - start > 2) chars[start] = Character.toUpperCase(chars[start]);
    }

    return String.valueOf(chars);
  }
}
