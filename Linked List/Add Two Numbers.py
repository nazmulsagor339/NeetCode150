# Problem Link: https://neetcode.io/problems/add-two-numbers/question?list=neetcode150

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum + l2.val
                l2 = l2.next
            sum += carry
            digit = sum % 10
            carry = sum // 10
            temp.next = ListNode(digit)
            temp = temp.next
        return head.next