# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.result = None

        def dfs(node):
            if not node or self.result is not None:
                return
            dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.result = node
            dfs(node.right)
        
        dfs(root)
        return self.result.val