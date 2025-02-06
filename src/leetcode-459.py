"""459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Constraints
-----------
1) 1 <= s.length <= 104
2) s consists of lowercase English letters.
"""


class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        (Approach)
        By doubling s (i.e., appending s to itself), we create a new string where any repetitive structure in s becomes more apparent.
        To prevent the doubled string from trivially containing s (as it always will), we remove the first and last characters of the doubled string.
        This ensures that if s appears again, it must be because it "wraps around" within the repeated pattern.

        (Rationale)
        If s can be constructed by repeating a substring, then its repetitive structure will align within the doubled string.
        After cutting off the first and last characters, s will still appear in the doubled string if and only if there exists a
        substring of s that can repeat to form s. If s does appear in this modified doubled string, it means there’s a repetition
        in s that effectively loops from the end of the first copy of s back to the start of the second copy of s.
        """
        return s in (s * 2)[1:-1]
