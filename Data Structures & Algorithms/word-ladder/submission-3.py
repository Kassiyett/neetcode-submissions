class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)        
        wordGraph = defaultdict(list) # 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                wordGraph[pattern].append(word)

        def bfs(word):
            res = 0
            q = deque([(word, 0)])
            visited = {word}
            
            while q:
                for _ in range(len(q)):
                    curr_word, depth = q.popleft()
                    if curr_word == endWord:
                        return res
                    
                    for i in range(len(curr_word)):
                        pattern = curr_word[:i] + "*" + curr_word[i+1:]
                        for nei in wordGraph[pattern]:
                            if nei not in visited:
                                visited.add(nei)
                                q.append((nei, depth+1))
                res += 1
            
        result = bfs(beginWord)
        return result + 1 if result is not None else 0