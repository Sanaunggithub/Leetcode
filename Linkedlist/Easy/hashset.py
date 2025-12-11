class ListNode:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 10**4
        self.set = [ListNode() for _ in range(self.size)]  

    def add(self, key: int) -> None:
        index = key % self.size
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = key % self.size
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next

        return False