class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total_fresh = 0
        time = 0

        queue = deque()
        visited = set()
        dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 2:
                    queue.append((x, y)) 
                    visited.add((x, y))
                if grid[x][y] == 1:
                    total_fresh += 1

        while queue and total_fresh > 0:
            for i in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                for dr_x, dr_y in dr:
                    x = curr_x + dr_x
                    y = curr_y + dr_y
                    if 0 <= x < row and 0 <= y < col and (x, y) not in visited and grid[x][y] == 1:
                        queue.append((x, y))
                        visited.add((x, y))
                        total_fresh -= 1
            time += 1

        return -1 if total_fresh != 0 else time