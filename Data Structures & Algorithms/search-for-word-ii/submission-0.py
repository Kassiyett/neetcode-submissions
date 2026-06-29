class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(x, y, node, word):
            if x < 0 or y < 0 or x == ROWS or y == COLS or (x, y) in visited or board[x][y] not in node.children:
                return

            visited.add((x, y))

            node = node.children[board[x][y]]
            word += board[x][y]
            if node.isEnd:
                res.add(word)
            dfs(x+1, y, node, word)
            dfs(x-1, y, node, word)
            dfs(x, y+1, node, word)
            dfs(x, y-1, node, word)

            visited.remove((x, y))

        for x in range(ROWS):
            for y in range(COLS):
                dfs(x, y, root, "")

        return list(res)
 
