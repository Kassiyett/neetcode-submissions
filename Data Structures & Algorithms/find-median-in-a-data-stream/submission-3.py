class MedianFinder:

    def __init__(self):
        # there will be 2 heaps
        # minheap, maxheap
        # so that when we add 3, 5, 2, 1
        # it should be, 2, 1 max    3, 5, min and the median will be 2 + 3/2 = 
        self.minHeap = [] # where big nums
        self.maxHeap = [] # where small nums

    def addNum(self, num: int) -> None:
        # add to minheap, when we have big num
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        # add to maxheap
        elif self.minHeap and num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            temp = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -temp)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -temp)
        print(self.maxHeap, self.minHeap)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0])/2