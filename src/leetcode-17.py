"""17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Constraints
-----------
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
"""


class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        """Getting Combos

        1. Simple Case: If not digits are given, return an empty list.

        2. Use a key map to associate digits to letters and initialize combos
           to just contain an empty string [""] to initially modify an empty combo on
           the first iteration.

        3. Consider all letters associated with the first digit, append each of these
           letters to each combo in the combos list. For example, take "23", the first
           iteration would consider "2" and see that "abc" are the associated letters,
           then we would end iteration with ["a","b","c"] because each time we add our
           new list of combos the old combos is unchanged. Continuing with this example,
           then next iteration results in ["ad","ae","af","bd","be","bf","cd","ce","cf"].
        """
        if not digits:
            return []
        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combos = [""]
        for digit in digits:
            letters = key[digit]
            combos = [combo + letter for combo in combos for letter in letters]

        return combos
