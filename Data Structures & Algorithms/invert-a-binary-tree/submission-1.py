# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        
        def invertHelper(node):
            if not node:
                return
            tempLeft = node.left
            node.left = node.right
            node.right = tempLeft

            invertHelper(node.left)
            invertHelper(node.right)

        invertHelper(root)
        return root