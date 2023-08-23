# Problem 2586: Count the Number of Vowel Strings in Range

"""
Constraints:

1) 1 <= words.length <= 1000
2) 1 <= words[i].length <= 10
3) words[i] consists of only lowercase English letters.
4) 0 <= left <= right < words.length

"""

class Solution:

    def vowelStrings(self, words: list[str], left: int, right: int) -> int:

        num : int = 0
        vowels : list = ['a','e','i','o','u']

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                num_of_vowel_strings += 1

        return num
