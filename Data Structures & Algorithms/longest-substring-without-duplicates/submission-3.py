class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "zxyzxyz"
        zxy
        z
        drop z
        add z
        xyz

        """
        max_l = 0
        l, r = 0, 0
        sub_s = set()
        for r in range(len(s)): #pwwkew
            while s[r] in sub_s: # p w : w, w
                sub_s.remove(s[l]) # w
                l += 1 # 1
            sub_s.add(s[r]) # pw, pw, wk
            max_l = max(max_l, (r - l + 1)) # p, pw, wwk
    
        return max_l
        