def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        mid = []
        curr = head

        size = 0

        while curr:
            size += 1
            curr = curr.next
        
        curr = head
        for i in range(size // 2):
            mid.append(curr.val)
            curr = curr.next

        if size % 2 != 0:
            curr = curr.next

        for val in reversed(mid):
            if curr.val != val:
                return False

            curr = curr.next

        return True