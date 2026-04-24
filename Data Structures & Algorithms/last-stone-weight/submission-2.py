class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            if firstStone < secondStone:
                newStone = firstStone - secondStone
                heapq.heappush(stones, newStone)
            if firstStone > secondStone:
                newStone = secondStone - firstStone
                heapq.heappush(stones, newStone)
        if not stones:
            return 0

        return -stones[0]