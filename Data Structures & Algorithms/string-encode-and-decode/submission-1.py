class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        word = ""
        res = []

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = s[i:j]
            l = int(length)
            word = s[j+1 : j+1+l]
            res.append(word)
            i = j + 1 + l
        return res