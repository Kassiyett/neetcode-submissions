class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        pacific_facing = []
        atlantic_facing = []
        pacific_reachable = [[False for _ in range(c)] for _ in range(r)]
        atlantic_reachable = [[False for _ in range(c)] for _ in range(r)]
        result = []

        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    pacific_facing.append((i, j))
                if i==r-1 or j == c-1:
                    atlantic_facing.append((i, j))
        
        dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def bfs(ocean_front, visited):
            q = deque(ocean_front) # stores cell coordinates (r, c)
            for nr, nc in ocean_front:
                visited[nr][nc] = True
    
            while q:
                curr_r, curr_c = q.pop()
                for dr_r, dr_c in dr:
                    nr = dr_r + curr_r
                    nc = dr_c + curr_c
                    if (0 <= nr < r and 0 <= nc < c and
                        heights[nr][nc] >= heights[curr_r][curr_c] and 
                        visited[nr][nc] == False):
                        q.append((nr, nc))
                        visited[nr][nc] = True

        bfs(pacific_facing, pacific_reachable)
        bfs(atlantic_facing, atlantic_reachable)
        
        for i in range(r):
            for j in range(c):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])

        return result