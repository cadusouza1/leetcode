class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    merged = ListNode()
    dummy = merged

    # Exausts one of the lists
    while list1 and list2:
        val = 0
        if list1.val <= list2.val:
            val = list1.val
            list1 = list1.next if list1 else None
        else:
            val = list2.val
            list2 = list2.next if list2 else None

        dummy.next = ListNode(val)
        dummy = dummy.next

    # Finish merging the other list that wasn't exausted
    while list1:
        dummy.next = ListNode(list1.val)
        dummy = dummy.next
        list1 = list1.next

    while list2:
        dummy.next = ListNode(list2.val)
        dummy = dummy.next
        list2 = list2.next

    return merged.next


def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    merged = mergeTwoLists(list1, list2)

    print("[", end=" ")
    while merged:
        print(f" {merged.val} ", end=" ")
        merged = merged.next
    print("]", end="")


if __name__ == "__main__":
    main()
