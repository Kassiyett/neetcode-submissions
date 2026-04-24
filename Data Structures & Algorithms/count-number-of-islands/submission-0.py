class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = set() # coordinates that are visited
        count = 0
        
        def dfs(x, y): # coordinates
            if ((x, y) in visited or 
                x not in range(r) or 
                y not in range(c) or 
                grid[x][y] == "0"):
                return
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count