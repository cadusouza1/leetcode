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
        nodes = []

        while head is not None:
            nodes.append(head)
            head = head.next

        return nodes[ceil(len(nodes) // 2)]
