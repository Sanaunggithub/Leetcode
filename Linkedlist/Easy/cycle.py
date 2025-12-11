def hasCycle(self, head):
        
    if head == None or head.next == None:
        return False

    lst = set()

    curr = head

    while curr != None:       
        if curr not in lst:
            lst.add(curr)
        
        else:
            return True
        curr = curr.next
    
    return False