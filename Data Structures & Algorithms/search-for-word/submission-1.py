from collections import deque
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(x, y, i):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            if (x, y) in visited:
                return False
            if board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited.add((x, y))
        
            found = dfs(x+1, y, i+1) or dfs(x, y+1, i+1) or dfs(x-1, y, i+1) or dfs(x, y-1, i+1)

            visited.remove((x, y))
            return found
            
        for x in range(len(board)):
            for y in range(len(board[0])):
                if word[0] == board[x][y]:
                    if dfs(x, y, 0):
                        return True
        
        return False