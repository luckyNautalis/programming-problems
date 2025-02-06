"""22. Generate Parenthesis
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints
-----------
1) 1 <= n <= 8
"""


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        """
        (Base Case)
        1. If the right count is equal to the number of pairs,
           then there are no more parenthesis to add.

        (Recursive Case I: Adding left parenthesis)
        2. If left count is less than number of pairs, then
           we can still add left parenthesis to the string.
           Call `wellForm(left + 1, right, s + '('))` to add a left
           parentheses, and increment the left count.


        (Recursive Case II: Adding right parenethesis)
        3. If the right count is less than the right count, then
           adding a right parentheses will keep the string well-formed.
           Call `wellForm(left, right + 1, s + ')')` to add a right
           parenthesis, and increment the right count.

        (Example: n = 2)
        wellForm(0, 0, "")
        ├── wellForm(1, 0, "(")
        │   ├── wellForm(2, 0, "((")
        │   │   └── wellForm(2, 1, "(()")
        │   │       └── wellForm(2, 2, "(())") // Base case, add to combos
        │   └── wellForm(1, 1, "()")
        │       └── wellForm(2, 1, "()(")
        │           └── wellForm(2, 2, "()()") // Base case, add to combos
        """

        def wellForm(left: int, right: int, s: str) -> str:
            if right == n:
                combos.append(s)
                return s

            if left < n:
                wellForm(left + 1, right, s + "(")

            if right < left:
                wellForm(left, right + 1, s + ")")

            return s

        combos = []
        wellForm(0, 0, "")
        return combos
