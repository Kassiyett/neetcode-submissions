# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        curr = root
        rootIndex = 0
        
        while inorder[rootIndex] != rootVal:
            rootIndex += 1
        
        root.left = self.buildTree(preorder[1:1 + rootIndex], inorder[:rootIndex])
        root.right = self.buildTree(preorder[1 + rootIndex:], inorder[rootIndex+1:])
        return root
