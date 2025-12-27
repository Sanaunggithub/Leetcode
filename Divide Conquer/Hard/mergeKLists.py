class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        return mergeLists(lists, 0, len(lists) - 1)


def mergeLists(lists, start, end):
    if start == end:
        return lists[start]

    mid = (start + end) // 2

    left = mergeLists(lists, start, mid)
    right = mergeLists(lists, mid + 1, end)

    return merge(left, right)


def merge(left, right):
    dummy = ListNode(-1)
    curr = dummy

    while left and right:
        if left.val <= right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

    if left:
        curr.next = left
    if right:
        curr.next = right

    return dummy.next