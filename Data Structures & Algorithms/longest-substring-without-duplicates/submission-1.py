class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "zxyzxyz"
        zxy
        z start again
        zxy
        z start again
        
        """
        max_l = 0
        l, r = 0, 0
        while r < len(s):
            sub_s = ""
            while r < len(s) and s[r] not in sub_s:
                sub_s += s[r]
                r += 1
            max_l = max(max_l, len(sub_s))
            l += 1
            r = l
            print(sub_s)
        return max_l
        