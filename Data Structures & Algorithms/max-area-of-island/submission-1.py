class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            if (x, y) in visited or x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                return 0
            visited.add((x, y))
            val =  1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1)
            return val
        
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    curr = dfs(x, y)
                    res = max(curr, res)
        return res