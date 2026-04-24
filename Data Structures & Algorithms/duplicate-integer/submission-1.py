class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
            if freq[n] > 1:
                return True
        return False