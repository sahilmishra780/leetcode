from typing import *
from collections import Counter
import heapq

class Solution:
    def isNStraightHandBruteForce(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        c = Counter(hand)
        while c:
            minVal = min(c.keys())
            for _ in range(groupSize):
                if minVal not in c:
                    return False
                c[minVal] -= 1
                if c[minVal] == 0:
                    del c[minVal]
                minVal += 1
        return True
    
    def isNStraightHandHeap(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        c = Counter(hand)
        h = list(c.keys())
        heapq.heapify(h)
        while c:
            minVal = h[0]
            for _ in range(groupSize):
                if minVal not in c:
                    return False
                c[minVal] -= 1
                if c[minVal] == 0:
                    if minVal != h[0]:
                        return False
                    del c[minVal]
                    heapq.heappop(h)
                minVal += 1
        return True

soln = Solution()
assert soln.isNStraightHandBruteForce([1,2,3,6,2,3,4,7,8], 3) == True
assert soln.isNStraightHandBruteForce([1,2,3,4,5], 4) == False
assert soln.isNStraightHandHeap([1,2,3,6,2,3,4,7,8], 3) == True
assert soln.isNStraightHandHeap([1,2,3,4,5], 4) == False