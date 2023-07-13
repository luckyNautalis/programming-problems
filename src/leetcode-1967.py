# Problem 1967: Number of Strings That Appear as Substrings in Word

"""
Constraints:

1) 1 <= patterns.length <= 100
2) 1 <= patterns.length <= 100
3) 1 <= word.length <= 100
4) patterns[i] and word consist of lowercase English letters

"""

class Solution:

    def numOfStrings(self, patterns: list[str], word: str) -> int:

        return len([pattern for pattern in patterns if pattern in word])

patterns = ["a","abc","bc","d"]; word = "abc"; s = Solution()
print(s.numOfStrings(patterns,word))
