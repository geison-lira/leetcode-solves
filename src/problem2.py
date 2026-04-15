# Imports and definitions (just for testing, DO NOT COPY THESE)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


# Actual solution below
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
        return dummy.next
