"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {} # node: 
        
        def dfs(n):
            if n in visited:
                return visited[n]

            copy_node = Node(n.val)
            visited[n] = copy_node

            for nei in n.neighbors:
                copy_node.neighbors.append(dfs(nei))
            return copy_node
            
        return dfs(node) if node else None