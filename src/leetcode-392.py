#!/usr/bin/env python3
# Problem 392: Is Subsequence
"""
Constraints:

1) 0 <= s.length <= 100
2) 0 <= t.length <= 10^4
3) s and t consist only of lowercase English letters.
"""

class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        i: int = 0; j: int = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
