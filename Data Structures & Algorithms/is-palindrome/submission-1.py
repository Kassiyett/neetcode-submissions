class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ''.join([c for c in s if c.isalnum()])
        letters = letters.lower()
        
        left = 0
        right = len(letters) - 1
        print(letters)
        while left <= right:
            if letters[left] != letters[right]:
                return False
            left += 1
            right -= 1
        return True