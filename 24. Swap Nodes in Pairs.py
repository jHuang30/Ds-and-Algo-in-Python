# Given a linked list, swap every two adjacent nodes and return its head.


# Example 1:


# Input: head = [1, 2, 3, 4]
# Output: [2, 1, 4, 3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]


# Constraints:

# The number of nodes in the list is in the range[0, 100].
# 0 <= Node.val <= 100

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = n1 = ListNode()
        dummy.next = head
        n2 = head

        while n2 and n2.next:
            next_node = n2.next.next
            n1.next = n2.next
            n1.next.next = n2
            n2.next = next_node
            n1 = n2
            n2 = next_node

        return dummy.next
