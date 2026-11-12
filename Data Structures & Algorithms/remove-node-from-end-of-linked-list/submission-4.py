# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head = [1,2,3,4], n = 2
        1: n = 2, prev = None
        2: n = 1 prev = 1
        3: n = 0 prev = 2
        [1->2->3->4]
        """
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        k = length - n
        print(length)

        curr = head
        prev = None
        if k == 0:
            return head.next
            
        while curr and k != 0: # [1->2]
            prev = curr # 1,
            curr = curr.next # 2
            k -=1 # 1
        if curr and prev:
            prev.next = curr.next
            return head

        return None