# Problem 9: Palindrome Number

"""
Constraints:

1) -231 <= x <= 231 - 1

"""

class Solution:

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
