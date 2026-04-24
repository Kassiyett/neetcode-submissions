# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(prevNode, currNode):
            if not currNode:
                return prevNode
            nextNode = currNode.next
            currNode.next = prevNode
            return reverseListHelper(currNode, nextNode)
        return reverseListHelper(None, head)