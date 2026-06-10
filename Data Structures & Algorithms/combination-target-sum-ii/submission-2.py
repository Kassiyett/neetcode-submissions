class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Returns the combination of unique elements that sum the target.
        """
        res = []
        candidates.sort()
        
        def dfs(idx, curr, s):
            if s == target:
                res.append(curr.copy())
                return
            if s > target or idx >= len(candidates):
                return
            
            val = candidates[idx]
            curr.append(val)
            dfs(idx + 1, curr, s + val)
            
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, curr, s)
        
        curr = []
        dfs(0, curr, 0)
        return res