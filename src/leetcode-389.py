#!/usr/bin/env python3
# Problem 389: Find the Difference
"""
Constraints:

1) 0 <= s.length <= 1000
2) t.length == s.length + 1
3) s and t consist of lowercase English letters.
"""
from typing import Dict

class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        scount: Dict[str, int] = {}
        tcount: Dict[str, int] = {}
        for c in s:
            if c in scount:
                scount[c] += 1
            else:
                scount[c] = 1

        for c in t:
            if c in tcount:
                tcount[c] += 1
            else:
                tcount[c] = 1

        for c in tcount:
            if c not in scount or tcount[c] > scount[c]:
                return c
