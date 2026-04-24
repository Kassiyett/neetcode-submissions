class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hash - for anagram ident
        maybe dict of keys and then their corresponding words

        act - adds
        pots - adds, add into the list as well
        tops - same as pots, added into the list
        """
        k = [0]*26 # 1, 0, 0, 0, 
        freq = defaultdict(list)

        for word in strs:
            k = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                k[index] += 1
            freq[tuple(k)].append(word)
        return list(freq.values())