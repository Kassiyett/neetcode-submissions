class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = defaultdict(int) # 0:1 means that a is repeated 1 times
        dict2 = defaultdict(int)

        # populate dict1
        for c in s1:
            dict1[ord(c) - ord('a')] += 1
    
        l = 0
        r = len(s1)
    
        for i in range(r):
            c = s2[i]
            dict2[ord(c) - ord('a')] += 1

        if dict1 == dict2:
            return True
        
        while r < len(s2):    
            dict2[ord(s2[l]) - ord('a')] -= 1
            if dict2[ord(s2[l]) - ord('a')] == 0:
                del dict2[ord(s2[l]) - ord('a')]
            
            dict2[ord(s2[r]) - ord('a')] += 1

            print(s2[l], s2[r], dict1, dict2)
            l += 1
            r += 1

            if dict2 == dict1:
                return True
    
        return False