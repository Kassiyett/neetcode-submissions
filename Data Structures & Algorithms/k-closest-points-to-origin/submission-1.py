class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        maxHeap = []
        result = []
        def distance(x, y):
            return math.sqrt(x**2 + y**2)
        
        for i, p in enumerate(points):
            x, y = p[0], p[1]
            d = distance(x, y)
            heapq.heappush(maxHeap, (-d, i))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while maxHeap:
            dis, res_id = heapq.heappop(maxHeap)
            result.append(points[res_id])
        return result