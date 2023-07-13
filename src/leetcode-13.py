# Problem 13: Roman to Integer

"""
Constraints:

1) 1 <= s.length <= 15
2) s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
3) It is guaranteed that s is a valid roman numeral in the range [1, 3999]

"""

import re

class Solution:

    roman_dict = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,
                        "L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}

    def romanToInt(self, s: str) -> int:

        arabic_numeral = 0

        pattern = "(" + "|".join(list(self.roman_dict.keys())) + ")"
        roman_numerals_listed = re.findall(pattern, s)

        for roman in roman_numerals_listed:
            arabic_numeral += self.roman_dict[roman]

        return arabic_numeral
