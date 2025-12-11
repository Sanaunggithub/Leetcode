def mergeTwoLists(list1, list2):
    dummy = ListNode() # Create a dummy node to simplify the merge process 
    tail = dummy   # tail is the head at the start

    while list1 and list2: # While both lists have nodes
        # we link instead of swapping because we are creating a new list.
        # So we append it.

        if list1.val < list2.val:
            tail.next = list1 # append list1 
            list1 = list1.next

        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next # we can move it now because we have linked list1 or list2

    # If anything is left in either list, attach it
    if list1:
        tail.next = list1

    elif list2:
        tail.next = list2

    return dummy.next # return the head because dummy.next is the real head


