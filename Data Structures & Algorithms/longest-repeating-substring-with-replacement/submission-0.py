class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        XYYX
count: X: 1
Y      X: 1, Y:1 
        """
        l = 0
        count = defaultdict(int) # number: count
        res = 0
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] += 1 
            maxf = max(maxf, count[s[r]]) # max element

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        
        return res