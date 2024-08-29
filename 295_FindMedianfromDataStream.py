from heapq import *
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if not self.left_heap:
            heappush(self.left_heap, -num)
        else:
            if -self.left_heap[0] < num:
                heappush(self.right_heap, num)
            else:
                heappush(self.left_heap, -num)

            if len(self.left_heap) > len(self.right_heap):
                heappush(self.right_heap, -heappop(self.left_heap))
            elif len(self.left_heap) < len(self.right_heap):
                heappush(self.left_heap, -heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        elif len(self.left_heap) < len(self.right_heap):
            return self.right_heap[0]
        else:
            return (-self.left_heap[0]+self.right_heap[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
