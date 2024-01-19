#!/usr/bin/env python3
# Problem 1071: Greatest Common Divisor of String

"""
Constraints:

1) 1 <= str1.length, str2.length <= 1000
2) str1 and str2 consist of English uppercase letters.

"""
from math import gcd

class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        We want to find the largest substring of both str1 and str2 s.t.
        the substring is a common divisor of str1 and str2, A.K.A. the gcd of strings.


        First we test if there exists a (greatest) common divisor by testing for additive commativity.
        Now if commutativity is satisfied, we know that there exists a common prefix. We find the largest common
        prefix that divides both strings by getting the common prefix of length equal to the gcd of both len(str1)
        and len(str2).
        """

        # GCD Of Strings Test: These strings must be additively commutative since a common prefix must occur subsequently in both strings.
        # If this is not triggered this means there must be a gcd of strings.
        if (str1 + str2) != (str2 + str1):
            return ''

        return str2[:gcd(len(str1), len(str2))]
