class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            divider = i
            while divider < len(s) and s[divider] != "#":
                divider += 1

            length = int(s[i:divider])
            word = s[divider+1:divider+1+length]
            res.append(word)

            i = divider + 1 + length
        return res