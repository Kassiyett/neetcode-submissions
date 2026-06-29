class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
    
    def dfs(self, curr, part_word):
        for i, c in enumerate(part_word):
            if c == '.':
                # trying all children
                for child in curr.children.values():
                    if self.dfs(child, part_word[i+1:]):
                        return True
                return False
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd

