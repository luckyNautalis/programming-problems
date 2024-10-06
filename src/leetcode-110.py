"""Problem 110: Balanced Binary Tree

Given a binary tree, determine if its height-balanced (abs(height(root.left), height(root.right)) = 0, 1)

Constraints:
    
    - The number of nodes in the tree range from [0, 5000]

    - (-10^4) <= node.val <= 10^4
"""

from typing import Optional


class Solution:

    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
