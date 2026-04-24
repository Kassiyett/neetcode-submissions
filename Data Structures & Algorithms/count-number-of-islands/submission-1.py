class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        
        def dfs(x, y):
            q = deque([(x, y)])
            visited.add((x, y))
            while q:
                x, y = q.pop()
                for dr_x, dr_y in directions:
                    curr_x, curr_y = dr_x + x, dr_y + y
                    if curr_x in range(len(grid)) and curr_y in range(len(grid[0])) and (curr_x, curr_y) not in visited and grid[curr_x][curr_y] == "1":
                        q.append((curr_x, curr_y))
                        visited.add((curr_x, curr_y))
                
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x, y) not in visited:
                    dfs(x, y)
                    count += 1
        
        return count