class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # n: count
        freq = [[] for i in range(len(nums) + 1)] # count: list of n
        
        for n in nums:
            count[n] += 1
        for n, val in count.items():
            freq[val].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res