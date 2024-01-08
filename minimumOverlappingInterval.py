from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort() # sort intervals by start time

        # As queries are iterated in sorted order store answers for each query in a map (query, length_for_query)
        mp = {}
        
        # Use a minheap to store (interval_length, interval_end)
        # This means the interval with the smallest length will come first
        # If intervals are of same length then the interval that ends first (i.e. smaller interval_end)
        # will be the minimum. This will make sure that an interval with an end in the future and 
        # more intersections with future query points is kept alive
        hp = [] 

        i = 0
        for q in sorted(queries):

            # find all overlapping intervals
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(hp, [right - left + 1, right])
                i += 1
            # find smallest interval overlapping with q
            while hp and hp[0][1] < q:
                heapq.heappop(hp)
            mp[q] = hp[0][0] if hp else -1
            
        return [mp[q] for q in queries]

# [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
print(Solution().minInterval([[1,4],[2,4],[3,6],[4,4]],[2,3,4,5]))