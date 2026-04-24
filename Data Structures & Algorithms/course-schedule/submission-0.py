class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        adj = defaultdict(list)
        for first, second in prerequisites:
            adj[second].append(first)

        # identify if there is a cycle
        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)

            for edge in adj[course]:
                if not dfs(edge):
                    return False

            path.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
