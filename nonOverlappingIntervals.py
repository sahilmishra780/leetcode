from typing import List

class Solution:
    def eraseOverlapIntervalsSortByStart(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < prevEnd:
                count += 1
                prevEnd = min(prevEnd, currEnd)
                """
                The idea in the above update is to keep the prev end time 
                the smallest so that we can later have maximum non-overlapping intervals.
                Updating the end time is sort of like deleting the interval that ends later i.e. the longer interval
                """
            else:
                prevEnd = currEnd
        return count
    
    def eraseOverlapIntervalsSortByEnd(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda interval: interval[1])
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < prevEnd:
                count += 1
            else:
                prevEnd = currEnd
        return count

soln = Solution()
assert soln.eraseOverlapIntervalsSortByStart([[1,2],[2,3],[3,4],[1,3]]) == 1
assert soln.eraseOverlapIntervalsSortByStart([[1,2],[1,2],[1,2]]) == 2
assert soln.eraseOverlapIntervalsSortByStart([[1,2],[2,3]]) == 0
assert soln.eraseOverlapIntervalsSortByStart([[1,100],[11,22],[1,11],[2,12]]) == 2
assert soln.eraseOverlapIntervalsSortByStart([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]) == 7

assert soln.eraseOverlapIntervalsSortByEnd([[1,2],[2,3],[3,4],[1,3]]) == 1
assert soln.eraseOverlapIntervalsSortByEnd([[1,2],[1,2],[1,2]]) == 2
assert soln.eraseOverlapIntervalsSortByEnd([[1,2],[2,3]]) == 0
assert soln.eraseOverlapIntervalsSortByEnd([[1,100],[11,22],[1,11],[2,12]]) == 2
assert soln.eraseOverlapIntervalsSortByEnd([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]) == 7
