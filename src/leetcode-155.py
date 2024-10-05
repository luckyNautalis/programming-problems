"""Problem 155: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

You must implement a solution with O(1) time complexity for each function.

Constraints:

     - (-2^31) <= val <= (2^31 -1)

     - Methods pop, top and getMin operations will always be called on non-empty stacks

     - At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:

    class _Node:

        def __init__(self, prev=None, min=None, val=None):
            """Initializes node for MinStack.

            Parameters
            ----------
            prev : _Node
                Pointer to previous node.
            min : int
                Minimum element from the node's level to the bottom node.
            val : int
                The node's value.

            """
            self.prev = prev
            self.min = min
            self.val = val

    def __init__(self, top_node=None):
        """Initializes MinStack.

        Parameters
        ----------
        top_node : _Node
            The top-most node of the stack.

        """
        self.top_node = top_node

    def __str__(self):
        """

        Returns
        -------
            String representation of MinStack.

        """
        stack = []
        current = self.top_node
        while current:
            stack.insert(0, current.val)
            current = current.prev

        return str(stack)

    def push(self, val: int) -> None:
        """Pushes a node on top of the stack.

        Parameters
        ----------
        val : int
            Value of node.

        """
        top_node = self._Node(prev=self.top_node, val=val)
        top_node.min = (
            top_node.prev.min if top_node.prev and val > top_node.prev.min else val
        )
        self.top_node = top_node

    def pop(self) -> None:
        """Removes the node on top of the stack."""
        self.top_node = self.top_node.prev

    def top(self) -> int:
        """Gets the top-most element.

        Returns
        -------
        int
            The top node's value.

        """
        return self.top_node.val

    def getMin(self) -> int:
        """Gets current minimum of the stack.

        Returns
        -------
        int
            Minimum value of the stack.

        """
        return self.top_node.min


# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]

stack = MinStack()

stack.push(-2)
print(stack)

stack.push(0)
print(stack)

stack.push(-3)
print(stack)

print("Min:", stack.getMin())

stack.pop()
print(stack)

print("Top:", stack.top())

print("Min:", stack.getMin())
