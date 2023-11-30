from typing import *
import heapq
class MedianFinder:

    def __init__(self):
        self.smaller, self.larger = [], []
        # smaller stores all the values <= median. Need immediate access to max of these values for the median. Uses maxHeap
        # larger stores all the values >= median.  Need immediate access to min of these values for the median. Uses minHeap

    def addNum(self, num: int) -> None:
        """
        invariants:
        1. max(smaller) <= min(larger)
        2. abs(len(smaller) - len(larger)) <= 1
        """
        if self.smaller and num > -self.smaller[0]:
            # num > max(smaller), therefore, belongs to larger
            heapq.heappush(self.larger, num)
        else:
            # either smaller is empty OR
            # num < max(smaller)
            # In both cases insert in smaller
            heapq.heappush(self.smaller, -num)

        if len(self.smaller) > len(self.larger) + 1:
            # shrink smaller
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))
        if len(self.larger) > len(self.smaller) + 1:
            # shrink larger
            heapq.heappush(self.smaller, -heapq.heappop(self.larger))

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        if len(self.larger) > len(self.smaller):
            return self.larger[0]
        return (-self.smaller[0] + self.larger[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

obj = MedianFinder()
obj.addNum(3)
obj.addNum(2)
obj.addNum(7)
obj.addNum(4)
print(obj.findMedian())