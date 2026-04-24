class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        width = len(grid)
        length = len(grid[0])
        dr = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        INF = 2147483647
        visited = set()
        queue = deque()  # stores (x, y)

        for x in range(width):
            for y in range(length):
                if grid[x][y] == 0:
                    queue.append((x, y, 0)) # x, y, distance
                    visited.add((x, y))

        while queue:
            curr_x, curr_y, distance = queue.popleft()
            for dr_x, dr_y in dr:
                x = dr_x + curr_x
                y = dr_y + curr_y
                if 0 <= x < width and 0 <= y < length and (x, y) not in visited:
                    if grid[x][y] == INF:
                        queue.append((x, y, distance + 1))
                        visited.add((x, y))
                        grid[x][y] = distance + 1