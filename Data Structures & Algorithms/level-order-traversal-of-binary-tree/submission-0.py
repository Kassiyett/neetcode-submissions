# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = []

        if not root:
            return result
            
        q.append(root)
        level = 0

        while q:
            result.append([])
            length = len(q)

            for i in range(length):
                node = q.pop(0)
                result[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return result