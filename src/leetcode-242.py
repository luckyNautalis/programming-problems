"""242. Valid Anagram

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Constraints
-----------
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. If the length s and t differ, then t cannot
           be an anagram of s.

        2. Make s a set of unique characters. Verify that
           the counts of each letter with that set occurs
           they same number of times in t as it does in s.

        string.count(c) counts the number of c occurs in string
        by yielding +1 at each occurence of c.
        """
        if len(t) != len(s):
            return False
        char_set = set(s)
        for c in char_set:
            if s.count(c) != t.count(c):
                return False
        return True
