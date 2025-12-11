class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(next=head) 

    # prev and curr are pointers. prev = dummy means prev now points to dummy.
    # so prev.val, prev.next, curr.val, curr.next

    prev, curr = dummy, head

    while curr:
        next = curr.next

        if curr.val == val:
            prev.next = next 
        
        else:
            prev = curr # move the whole goddamn prev

        curr = next # move the whole goddamn curr
    
    return dummy.next
