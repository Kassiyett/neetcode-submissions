class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make freq map for each chars in str
        # then append it to hashmap -> freq:str
        # go over each value and add it to res
        res = []
        freq = defaultdict(list) # freq: list of str
        for s in strs:
            curr = [0]*26
            for c in s:
                i = ord(c) - ord("a")
                curr[i] += 1
            # print(s, curr)
            # curr_freq = "".join(str(c) for c in curr)
            # print(s, curr_freq)
            freq[tuple(curr)].append(s)
        # print(freq)
        
        for val in freq.values():
            res.append(val)
        # res.sort()
        return res