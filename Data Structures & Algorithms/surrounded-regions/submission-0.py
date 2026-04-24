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
        
        def bfs(pos):
            q = deque() # storing (x, y)
            q.append(pos)
            visited.add(pos)
            notSurrender.append(pos)

            while q:
                currX, currY = q.pop()
                for drX, drY in dr:
                    x = currX + drX
                    y = currY + drY
                    if (0 <= x < r and 0 <= y < c and board[x][y] == "O" and (x, y) not in visited):
                        q.append((x, y))
                        visited.add((x, y))
                        notSurrender.append((x, y))
        
        for pos in border:
            bfs(pos)
        
        for x in range(r):
            for y in range(c):
                if (x, y) not in notSurrender and board[x][y] == "O":
                    board[x][y] = "X"