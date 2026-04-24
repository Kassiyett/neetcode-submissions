# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # half of the array

        prev = None # start of the half of the Nodes
        curr = slow.next
        slow.next = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        first, second = head, prev
        while second:
            f, s = first.next, second.next
            first.next = second
            second.next = f
            first, second = f, s