class Solution:
    def isValid(self, s: str) -> bool:
        chars = deque()
        signs = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in signs.values():
                chars.append(c)
            elif c in signs:
                if not chars or chars[-1] != signs[c]:
                    return False
                chars.pop()
        if len(chars) == 0:
            return True
        return False