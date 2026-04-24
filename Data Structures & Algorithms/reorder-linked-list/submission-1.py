# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head
        dummy = ListNode(-1, head)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half of the list
        curr = slow.next
        slow.next = None
        prev = None
        # reversing second half
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2