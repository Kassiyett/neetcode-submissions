class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        res = []
        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                sub = s[start:end+1]

                if isPalindrome(sub):
                    path.append(sub)
                    dfs(end + 1, path)
                    path.pop()
        dfs(0, [])
        return res
