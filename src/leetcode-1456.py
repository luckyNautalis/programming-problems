"""1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints
-----------
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

"""


class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        max_count = count = sum(map(lambda c: c in "aeiou", s[:k]))
        for i in range(len(s) - k):
            if s[i] in "aeiou":
                count -= 1
            if s[i + k] in "aeiou":
                count += 1
            max_count = max(count, max_count)

        return max_count
