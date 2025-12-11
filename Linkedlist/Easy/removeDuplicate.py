def deleteDuplicates(self, head):
    if not head:
        return None

    dummy = ListNode(None) # always initialize with None to avoid edge case
    prev, curr = dummy, head

    while curr:
        if curr.val != prev.val:
            prev.next = curr
            prev = prev.next              

        curr = curr.next

    prev.next = None # ends the linked list
    return dummy.next