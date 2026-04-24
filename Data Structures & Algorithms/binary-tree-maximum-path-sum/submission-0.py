# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        
        # return max path without split
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftMax = max(dfs(root.left), 0) # we compare to 0 because there can be negative values
            rightMax = max(dfs(root.right), 0)

            # compute max path with split
            res = max(res, root.val + leftMax + rightMax)

            # we are returning maxpath without split
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res