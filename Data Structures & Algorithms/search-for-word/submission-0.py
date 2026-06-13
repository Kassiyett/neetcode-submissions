from collections import deque
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        res = False

        def dfs(r, c, i):  
            nonlocal res

            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return

            if (r, c) in visited:
                return

            if i == len(word) - 1:
                res = True
                return
            
            visited.add((r, c))

            dfs(r + 1, c, i+1)
            dfs(r, c+1, i+1)
            dfs(r - 1, c, i+1)
            dfs(r, c - 1, i+1)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    dfs(r, c, 0)

        return res
