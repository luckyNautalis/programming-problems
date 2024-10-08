"""Problem 1382: Balance Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Constraints:
    - The number of nodes in the tree is in the range [1, 10^4].
    - 1 <= node.val <= 10^5

"""


class Solution:

    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def inorder(self, root: TreeNode) -> List[TreeNode]:
        stack = []
        inorder = []

        current = root
        while len(stack) != 0 or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current)
            current = current.right

        return inorder

    def balanceInorder(self, inorder: List[TreeNode]) -> TreeNode:
        if not inorder:
            return None

        mid = len(inorder) // 2
        root = inorder[mid]
        root.left = self.balanceInorder(inorder[:mid])
        root.right = self.balanceInorder(inorder[mid + 1 :])

        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.balanceInorder(self.inorder(root))
