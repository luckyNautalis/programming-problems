
/**
 * Problem 19: Remove the Nth Node From End of List
 *
 * Given the head of a linked list, remove the nth node from the end of the list
 * and return its head.
 *
 * Constraints:
 * - The number of nodes in the list is sz.
 * - 1 <= sz <= 30
 * - 0 <= Node.val <= 100
 * - 1 <= n <= sz
 */
import java.util.ArrayList;

class Solution {

    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ArrayList<ListNode> nodeList = new ArrayList<>();
        ListNode current = head;

        while (current != null) {
            nodeList.add(current);
            current = current.next;
        }

        int size = nodeList.size();
        if (size == n)
            return head.next;

        ListNode prev = nodeList.get(size - n - 1);
        prev.next = prev.next.next;

        return head;
    }
}
