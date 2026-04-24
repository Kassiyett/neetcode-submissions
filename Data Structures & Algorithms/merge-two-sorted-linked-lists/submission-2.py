# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        check 1 and 1
        connect, go to next,

        """
        dummy = ListNode(-1)
        newList = dummy

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                newList.next = curr1
                newList = newList.next
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                newList.next = curr2
                newList = newList.next
                curr2 = curr2.next

        if curr1:
            newList.next = curr1
        else:
            newList.next = curr2

        return dummy.next