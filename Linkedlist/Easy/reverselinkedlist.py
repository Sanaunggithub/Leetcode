def reverseList(self, head):
    # If the list is empty or has only one node, 
    if not head or not head.next:
        return head

    prev, current = None, head

    while current:
        nxt = current.next # becuz we will change current.next 
        current.next = prev
        prev = current  
        current = nxt

    return prev