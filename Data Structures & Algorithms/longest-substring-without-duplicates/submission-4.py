class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        zxyzxyz
        zxyz
        xyz
        """
        left = 0
        charSet = set()
        max_length = 0

        for right in range(len(s)):
            print(s[left:right], max_length, charSet)
            
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_length = max(right - left + 1, max_length)
        
        return max_length
