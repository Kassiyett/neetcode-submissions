class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        edge_cnt = {}
        
        for i in range(n):
            edge_cnt[i] = len(adj[i])
            if len(adj[i]) == 1:
                q.append(i)

        while q:
            if n <= 2:
                return list(q)
            
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        q.append(nei)
