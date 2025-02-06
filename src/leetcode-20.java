
/* 20. Valid Parentheses
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 *
 * An input string is valid if:
 *
 * 1) Open brackets must be closed by the same type of brackets.
 * 2) Open brackets must be closed in the correct order.
 * 3) Every close bracket has a corresponding open bracket of the same type.
 *
 * Constraints
 * -----------
 * 1) 1 <= s.length <= 10^4
 * 2) s consists of parentheses only '()[]{}'.
 */

import java.util.Stack;

class Solution {

    public boolean isValid(String s) {
        /*
         * Stack Approach
         * 
         * 1. Initialize a stack to process the brackets.
         *
         * 2. Iterate through the string s: If we encounter an
         * opening bracket, then push the corresponding closing bracket
         * onto the stack. Then the next closing bracket we get in iteration
         * must match the top of the stack for the string to be valid.
         * The string is invalid if the stack is empty before finishing iteration
         * or when the next closing bracket does not match the top the stack, so
         * we return false here.
         *
         * 3. Follow step (2) and by the end we should find matches for every closing
         * bracket popped off our stack. So, the stack should be empty, and we return
         * true if this is the case.
         */
        Stack<Character> stack = new Stack<>();
        for (char b : s.toCharArray()) {
            if (b == '(')
                stack.push(')');
            else if (b == '{')
                stack.push('}');
            else if (b == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != b)
                return false;
        }
        return stack.isEmpty();
    }
}
