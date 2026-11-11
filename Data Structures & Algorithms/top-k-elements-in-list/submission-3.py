class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create freq map -> num:count
        # make a heap? - keep the len as k
        #     if more len more than k -> pop and add the heapq
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        heap = []
        for num, count in freq.items():
            if len(heap) >= k:
                if heap[0][0] < count: # smallest element in heap is smaller than val, then we remove that el and add bigger one
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, (count, num))
        # print(heap)
        res = []
        for count, num in heap:
            res.append(num)
        return res