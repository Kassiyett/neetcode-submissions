# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # first merge the first two then others
        def mergeLists(l1, l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return dummy.next

        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = mergeLists(lists[i-1], lists[i])
    
        return lists[-1]