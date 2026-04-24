class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1,7,2,5,4,7,3,6]
        if l < r
        more l
        if l > r
        more r
        """
        l, r = 0, len(heights) - 1
        res = 0
        
        while l < r:
            x = min(heights[l], heights[r])
            res = max(res, ((r - l)*x))
            print(l, r)
            print(res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res