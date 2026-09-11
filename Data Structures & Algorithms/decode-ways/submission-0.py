class Solution:
    def numDecodings(self, s: str) -> int:
        """
        base: if theres anything to work with, then add
        if
        """
        one, two = 1, 0 # one = dp[i+1], two = dp[i+2]
        

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                # dp[i] = dp[i+1]
                curr = one

            if i < len(s) - 1:
                if (s[i] == "1" or (s[i] == "2" and s[i+1] < "7")):
                    # dp[i] += dp[i+2]
                    curr += two
            one, two = curr, one
                
        return one