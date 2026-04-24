class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre) # course: prepeq

        visited = set() # 0
        cycle = set() #
        result = [] # 0

        def dfs(course):
            if course in cycle: 
                return False
            if course in visited: 
                return True
            
            cycle.add(course)
            for edge in adj[course]:
                if dfs(edge) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return result
        

