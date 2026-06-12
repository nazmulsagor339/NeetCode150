# Problem Link: https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        previous = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next_node
        return previous