class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list
        # course: prereq
        adj = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        
        visited = {}
        result = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            result.append(c)
        
        for c in adj:
            if dfs(c):
                return []
        return result
            