"""Problem 104: Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum dpeth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:
    
    - The number of nodes in the tree is in range [0, 10^4].

    - (-100) <= Node.val <= 100
"""
from typing import Optional

class Solution:

    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
