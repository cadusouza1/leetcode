from math import ceil
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(
        self, head: ListNode | None
    ) -> ListNode | None:
        tail = head
        len = 0

        while tail is not None:
            tail = tail.next
            len += 1

        for _ in range(0, len // 2):
            head = head.next

        return head


