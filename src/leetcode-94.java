
/*
 * Problem # 94: Binary Tree Inorder Traversal
 *
 * Given the root of a binary tree, return the inorder traversal of its nodes'
 * values.
 */
import java.util.List;
import java.util.Stack;

class Solution {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<TreeNode> stack = new Stack<>();
        List<Integer> inorder = new Stack<>();
        TreeNode current = root;

        while (!stack.isEmpty() || current != null) {
            while (current != null) {
                stack.addLast(current);
                current = current.left;
            }

            current = stack.removeLast();
            inorder.addLast(current.val);

            current = current.right;
        }
        return inorder;
    }
}
