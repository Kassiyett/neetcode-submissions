class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        # a: (b, 4) 
        for i, (u, v)in enumerate(equations):
            adj[u].append((v, values[i]))
            adj[v].append((u, 1/values[i]))

        
        def bfs(start, end):
            if start not in adj or end not in adj:
                return -1
            q = deque([(start, 1)])
            visited = set([start]) 
            # q = (node, weight)
            while q:
                node, w = q.popleft()
                if node == end:
                    return w
                for nei, wNei in adj[node]:
                    if nei not in visited:
                        q.append((nei, w*wNei))
                        visited.add(nei)
            return -1
        
        result = []
        for a, b in queries:
            result.append(bfs(a, b))
        return result
        