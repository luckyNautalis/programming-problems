"""504. Base 7

Given an integer num, return a string of its base 7 representation.

Constraints
-----------

1) -10^7 <= num <= 10^7
"""


class Solution:

    def convertToBase7(self, num: int) -> str:
        """Division Algorithm
        (0 Case)
        1. If we num is 0, then return "0"

        (Initialization)
        2. Define a sign variable to be an empty string "" if the
           number is non-negative, otherwise take it to be "-".
           Define a quotient variable to be the absolute value
           of the number, this is to apply the division algorithm
           properly when passed negative numbers. Define a result variable
           for the string representation of base 7, the sign will be put in
           front of the result at the end of the division algorithm

        (Div Algo)
        3. While the quotient is greater than 0:
            - Assign result to be the remainder (quotient mod 7) + result
            - Assign the quotient to be the floor division by 7

        (Stop)
        4. Return the sign + result, if the number passed is non-negative, then
          the sign is "", otherwise the sign is "-".
        """

        if num is 0:
            return "0"

        sign = "" if num >= 0 else "-"
        quotient = abs(num)
        result = ""

        while quotient > 0:
            result = str(quotient % 7) + result
            quotient //= 7
        return str(sign) + result
