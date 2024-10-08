
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
        /*
         * A space-efficient approach where we only keep track
         * of a two nodes, n units apart.
         */
        ListNode prev = head;
        ListNode last = head;

        // Distance apart should be n+1 to skip nth node from end.
        int delta = 0;
        while (last != null) {
            last = last.next;
            delta++;
            if (delta > n + 1)
                prev = prev.next;
        }

        if (delta == n)
            return head.next;

        prev.next = prev.next.next;
        return head;
    }
}
