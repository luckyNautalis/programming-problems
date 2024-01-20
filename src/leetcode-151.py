#!/usr/bin/env python3
# Problem 151: Reverse Words in a String
"""
Constraints:
1) 1 <= s.length <= 104
2) s contains English letters (upper-case and lower-case), digits, and spaces ' '.
3) There is at least one word in s.
"""
from typing import List

class Solution:

    def reverseWords(self, s: str) -> str:
        """
        Split the strings into a list and reverse. Loop through this reversed list and if the
        item is a non-space character add it to rev_words. Then we can join together the words
        in rev_words by a space.
        """
        rev_list: List[str] = s.split(' ')[::-1]
        rev_words: List[str] = []
        for c in rev_list:
            if len(c):
                rev_words.append(c)

        return ' '.join(rev_words)
