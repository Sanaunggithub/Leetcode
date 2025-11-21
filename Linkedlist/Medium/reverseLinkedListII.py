def reverseBetween(self, head, left, right):
           
    # 1) reach node at position "left"
    dummy = ListNode(0, head)
    leftPrev, curr = dummy, head
    for i in range(left - 1):
        leftPrev = curr
        curr = curr.next

    # Now curr = "left", leftPrev = "node before left"
    # 2) reverse from left to right
    prev = None
    for i in range(right - left + 1):
        tmpNext = curr.next
        curr.next = prev
        prev = curr
        curr = tmpNext
    
    # 3) update pointers
    leftPrev.next.next = curr
    leftPrev.next = prev

    return dummy.next