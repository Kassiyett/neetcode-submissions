# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [0, 1, 2, 3, 4, 5, 6]
        0, 6,1,5,2,4,3

        0,1,3
        0,3,1

        0, 1, 2,       6, 4, 5, 3
        0 6 1 4 2 5,3

        3 -> 4-> 5-> 6
        3 <- 4 -> 5 -> 6

        get length 
        traverse till half
        detach half = second half
        reverse right
        
        merge first and second halves?

        """
        curr = head
        length = 0 
        while curr:
            curr = curr.next
            length+=1
        half = (length + 1) // 2 # floor num
        
        left, right= head, head
        prev = None
        for _ in range(half):
            prev = right
            right = right.next
        # detach left
        prev.next = None

        # reverse right
        curr = right
        reverse = right
        prev = None
        # <- 3 <- 4 <- 5 6
        while curr: # 3, 4,5,6
            temp = curr.next # 4,5,6,None
            curr.next = prev # 3 -> None, 4 -> 3
            prev = curr # 3, 4, 5, 6
            curr = temp # 4, 5, 6, None
        second = prev
        first = left

        # merge
        while second and first: #0-> 6->  1-> 2,  4-> 5-> 3
            tempFirst = first.next # 2
            tempSecond = second.next # 5

            first.next = second #1-> 2, 0-> 6-> 4-> 5-> 3
            second.next = tempFirst #0-> 6->1-> 2,  4-> 5-> 3

            second = tempSecond # 4
            first = tempFirst # 1
        
