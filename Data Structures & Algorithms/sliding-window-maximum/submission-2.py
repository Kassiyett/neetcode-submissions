class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,2,1,0,4,2,6]
        res = []
        q = deque()
        
        for r in range(len(nums)):
            val = nums[r]
            # remove expired idx
            while q and q[0] <= r - k:
                q.popleft()
            
            #remove vals smaller
            while q and nums[q[-1]] < val:
                q.pop()

            q.append(r)
            
            if r >= k - 1:
                res.append(nums[q[0]])

        return res
