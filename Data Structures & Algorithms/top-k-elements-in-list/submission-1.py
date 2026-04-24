class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        minheap
        (num, count)

        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        minHeap = []
        for num, val in counts.items():
            heapq.heappush(minHeap, (val, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res