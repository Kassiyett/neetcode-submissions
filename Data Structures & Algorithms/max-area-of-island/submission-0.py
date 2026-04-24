class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width = len(grid)
        length = len(grid[0])
        max_area = 0
        visited = set() # set of (x, y)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


        def dfs(x, y):
            visited.add((x, y))
            area = 1
            for dr_x, dr_y in directions:
                curr_x = x + dr_x
                curr_y = y + dr_y
                if 0 <= curr_x < width and 0 <= curr_y < length and (curr_x, curr_y) not in visited:
                    if grid[curr_x][curr_y] == 1:
                        area += dfs(curr_x, curr_y)
            return area

        for x in range(width):
            for y in range(length):
                if grid[x][y] == 1:
                    max_area = max(dfs(x, y), max_area)
        return max_area