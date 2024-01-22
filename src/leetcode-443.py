#!/usr/bin/env python3
# Problem 443: String Compression
"""
Constraints:

1) 1 <= chars.length <= 2000
2) chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

from typing import List

class Solution:

    def compress(self, chars: List[str]) -> int:
        chars += ' '
        n: int = 1
        i: int = 0
        while i < len(chars) - 1:
            if chars[i] == chars[i+1]:
                n += 1
            elif n > 9:
                # Replace the next (n-1) spots with digits of n (which is greater or equal to 2).
                chars[i + 1 - (n - 1) : i + 1] = list(str(n))
                # Step back (n - 1) spots and step up with the digit length from the second digit to the last of n (at least a step up of 1).
                # We want to step up with the length from second to last digit of n because if the chars[i] != chars[i+1], then we assume that
                # at least one digit will be appended which is one spot after some leading character in the iteration. So, when we see a n with
                # 2 or more digits, then we must add that portion back to be consecutive in the modified chars array.
                i -= (n -  2) - (len(str(n)) - 1)
                n = 1
            elif n > 1:
                # Replace the next (n-1) spots with the digits of n (which is just one here).
                chars[i + 1 - (n - 1): i + 1] = list(str(n))
                # Step back (n - 1) spots.
                i -= n - 2
                n = 1
            i += 1
        del chars[-1]

        return len(chars)
