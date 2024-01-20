#!/usr/bin/env python3
# Problem 345: Reverse Vowels of a String
"""
Constraints:

1) 1 <= s.length <= 3 * 105
2) s consist of printable ASCII characters.
"""
from typing import List

class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels: List[str] = ['A', 'E', 'I', 'O', 'U',
                             'a', 'e', 'i', 'o', 'u']
        rv: List[str] = [*s]
        i: int = 0
        j: int = len(s) - 1

        while i < j:

            if rv[i] in vowels:

                while rv[j] not in vowels:
                    j -= 1

                rv[i], rv[j] = s[j] ,s[i]
                j -= 1

            i += 1

        return ''.join(rv)
