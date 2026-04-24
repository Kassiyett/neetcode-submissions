class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = [] # store the pos of borders
        w = len(board)
        h = len(board[0])
        for x in range(w):
            for y in range(h):
                if ((x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) -1)
                    and board[x][y] == "O"):
                    border.append((x, y))

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        nonSurrender = []
        def dfs(pos):
            curr_x, curr_y = pos
            if pos in visited:
                return
            visited.add(pos)
            for dr_x, dr_y in directions:
                x, y = curr_x + dr_x, curr_y + dr_y
                if (0 <= x < w and 0 <= y < h and board[x][y] == "O"):
                    dfs((x, y))
            nonSurrender.append(pos)

        for pos in border:
            dfs(pos)

        print(nonSurrender)

        for x in range(w):
            for y in range(h):
                if ((x, y) not in nonSurrender and board[x][y] == "O"):
                    board[x][y] = "X"