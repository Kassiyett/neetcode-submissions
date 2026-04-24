# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        
        """
        
        res = []

        if not root:
            return res
            
        q = collections.deque()
        q.append(root)
        level = 0

        while q:
            l = len(q)
            res.append([])

            for _ in range(l):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                res[level].append(curr.val)

            level += 1
        return res