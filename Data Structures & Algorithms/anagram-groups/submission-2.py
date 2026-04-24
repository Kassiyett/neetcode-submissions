class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # char tuple: words list
        for s in strs:
            letters = [0] * 26
            # create key
            for c in s:
                letters[ord(c) - ord('a')] += 1
            res[tuple(letters)].append(s)
        return list(res.values())