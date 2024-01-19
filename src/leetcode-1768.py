#!/usr/bin/env python3
# Problem 1768: Merge Strings Alternately

"""
Constraints:

1) 1 <= word1.length, word2.length <= 100

2) word1 and word2 consist of lowercase English letters.
"""

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged: str = ""
        p1: int = 0
        p2: int = 0

        for l in (word1 + word2):

            if p1 < len(word1):
                merged += word1[p1]
                p1 += 1

            if p2 < len(word2):
                merged += word2[p2]
                p2 +=1

        return merged
