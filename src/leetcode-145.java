
/*
 * Problem # 145: Binary Tree Postorder Traversal
 *
 * Given the root of a binary tree, return the postorder traversal of its nodes' values.
 */
import java.util.List;
import java.util.LinkedList;
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

    public List<Integer> postorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> postorder = new LinkedList<>(); // O(1) reversed for doubly-linked list
        TreeNode current = root;

        stack.push(current);
        while (!stack.isEmpty() && current != null) {
            current = stack.pop();
            postorder.addFirst(current.val);

            if (current.left != null)
                stack.addLast(current.left);
            if (current.right != null)
                stack.addLast(current.right);
        }
        return postorder;
    }
}
