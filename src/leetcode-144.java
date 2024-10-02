
/*
 * Problem # 144: Binary Tree Preorder Traversal
 *
 * Given the root of a binary tree, return the preorder traversal of its nodes' values.
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

    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> preorder = new Stack<>();
        TreeNode current = root;

        stack.push(current);
        while (!stack.isEmpty() && current != null) {
            current = stack.pop();
            preorder.addLast(current.val);

            if (current.right != null)
                stack.push(current.right);
            if (current.left != null)
                stack.push(current.left);
        }
        return preorder;
    }
}
