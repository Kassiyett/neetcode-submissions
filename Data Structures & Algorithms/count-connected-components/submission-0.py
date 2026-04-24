class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # edges[i] = [a, b]
        adj = {key: [] for key in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for edge in adj[node]:
                if edge == parent:
                    continue
                dfs(edge, node)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count

