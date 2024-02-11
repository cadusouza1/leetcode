class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    if head:
        unique = ListNode(head.val)
    else:
        return None

    dummy = unique

    while head:
        if head.val != dummy.val:
            dummy.next = ListNode(head.val)
            dummy = dummy.next

        head = head.next

    return unique.next
