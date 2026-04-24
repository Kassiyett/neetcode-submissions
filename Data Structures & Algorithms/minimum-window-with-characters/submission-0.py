class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_sbstr = ""
        l = 0
        target = defaultdict(int)
        window = defaultdict(int)
        matched = 0
        needed = len(t)
        min_len = float("inf")

        # target dict
        for c in t:
            target [c] += 1

        # window
        for r in range(len(s)):
            
            c = s[r]
            # start adding only the nums in target needed to window
            if c in target:
                window[c] += 1
                
                if window[c] <= target[c]:
                    matched += 1
            
            print(l, r,  window, matched)
            # shrinking the window when we are done with all target
            while matched == needed:
                if r - l + 1 <= min_len:
                    min_len = r - l + 1 
                    min_sbstr = s[l:r+1]
                
                if s[l] in target:
                    if window[s[l]] == target[s[l]]:
                        matched -= 1
                    window[s[l]] -= 1
                
            
                print(matched, window,  s[l:r+1], min_sbstr)
                l += 1
            
        return min_sbstr