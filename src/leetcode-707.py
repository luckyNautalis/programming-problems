"""Problem 707: Design Linked List (Doubly-Linked List Implementation)

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    - MyLinkedList() Initializes the MyLinkedList object.

    - int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.

    - void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

    - void addAtTail(int val) Append a node of value val as the last element of the linked list.

    - void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.

    - void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Constraints:
    - 0 <= index, val <= 1000
    - Please do not use the built-in LinkedList library. At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""


# TODO: Make Doubly-Linked List w/ dummy
class MyLinkedList:

    class _Node:

        def __init__(self, prev=None, next=None, val=None):
            self.prev = prev
            self.next = next
            self.val = val

    def __init__(self):
        self.dummy = self._Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.size = 0

    def __str__(self):
        lst = []
        current = self.dummy.next
        while current:
            if current.val == None:
                break
            lst.append(str(current.val))
            current = current.next

        return " <-> ".join(lst)

    def getNode(self, index: int) -> _Node:
        # Traverse from the end of least traversals
        size = self.size
        current = self.dummy.next  # Assumption at index=0
        if index < size // 2:
            for _ in range(index):
                current = current.next
        else:
            current = self.dummy
            for _ in range(size - index):
                current = current.prev

        return current

    def get(self, index: int) -> int:
        size = self.size
        if index < 0 or index >= size:
            return -1

        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        new_head = self._Node(val=val)
        old_head = self.dummy.next
        new_head.next = old_head
        old_head.prev = new_head
        self.dummy.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = self._Node(val=val)
        old_tail = self.dummy.prev
        new_tail.prev = old_tail
        old_tail.next = new_tail
        self.dummy.prev = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        size = self.size
        if index < 0 or index > size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == size:
            self.addAtTail(val)
            return

        new_node = self._Node(val=val)
        next_node = self.getNode(index)
        new_node.prev = next_node.prev
        new_node.next = next_node
        next_node.prev = new_node
        new_node.prev.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        size = self.size
        if index < 0 or index >= size:
            return

        del_node = self.getNode(index)
        if size == 1:
            del_node.val = None
        else:
            if index == 0:
                del_node.next.prev = self.dummy
                self.dummy.next = del_node.next
            if index == size - 1:
                del_node.prev.next = self.dummy
                self.dummy.prev = del_node.prev
            if 0 < index < size - 1:
                prev_node = del_node.prev
                next_node = del_node.next
                prev_node.next = del_node.next
                next_node.prev = del_node.prev
        self.size -= 1


# ["MyLinkedList","addAtHead","addAtIndex","get"]
# [[],[2],[0,1],[1]]
ll = MyLinkedList()

ll.addAtHead(2)
print(ll)

ll.addAtIndex(0, 1)
print(ll)

print(f"Val at index=1: {ll.get(1)}")
