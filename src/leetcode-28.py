"""Problem 28: Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints

1) 1 <= haystack.length, needle.length <= 10^4
2) haystack and needle consist of only lowercase english letters

"""


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)

        for i in range(h - n + 1):
            for j in range(n):
                if needle[j] != haystack[i + j]:
                    break

                if j == n - 1:
                    return i

        return -1
