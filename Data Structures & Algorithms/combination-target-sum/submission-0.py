class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            if remaining < 0 or i >= len(nums):
                return 
            
            curr.append(nums[i])
            dfs(i, curr, remaining - nums[i])
            curr.pop()
            dfs(i+1, curr, remaining)
        
        dfs(0, [], target)
            
        return res