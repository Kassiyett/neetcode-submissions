class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = []
        r = len(board)
        c = len(board[0])
        visited = set()
        notSurrender = []
        dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for x in range(r):
            for y in range(c):
                if((x == 0 or y == 0 or x == r-1 or y == c-1) and board[x][y] == "O"):
                    border.append((x, y))
        
        def dfs(pos):
            x, y = pos
            if (x, y) in visited:
                return
            visited.add((x, y))
            notSurrender.append((x, y))
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == "O":
                    dfs((nx, ny))

        for pos in border:
            dfs(pos)
        
        for x in range(r):
            for y in range(c):
                if (x, y) not in notSurrender and board[x][y] == "O":
                    board[x][y] = "X"