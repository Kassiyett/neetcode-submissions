class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {c : [] for c in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set() #  0 
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for edge in adj[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n