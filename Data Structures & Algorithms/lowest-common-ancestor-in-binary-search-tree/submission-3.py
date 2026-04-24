# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        5, check children, not p or q, move on,
        p < root.val < q
        return root
        if max(p, q) < root.val
        go left
        if min(p, q) > root.val
        go right

        """
        while root:
            if min(p.val, q.val) <= root.val <= max(p.val, q.val):
                return root
            elif max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right

        return None