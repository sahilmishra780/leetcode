from typing import List

class Solution:
    def isCurrBeforeNew(self, currInterval, newInterval):
        newStart, newEnd = newInterval
        currStart, currEnd = currInterval
        return currEnd < newStart

    def isCurrOverlapNew(self, currInterval, newInterval):
        newStart, newEnd = newInterval
        currStart, currEnd = currInterval
        return currStart <= newEnd

    def mergeInterval(self, currInterval, newInterval):
        newStart, newEnd = newInterval
        currStart, currEnd = currInterval
        return [min(currStart, newStart), max(currEnd, newEnd)]

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i, n = 0, len(intervals)

        # add all intervals that come before newInterval
        # currInterval's end is before newInterval's start
        while i < n and self.isCurrBeforeNew(intervals[i], newInterval):
            ans.append(intervals[i])
            i += 1
        
        # merge all intervals that overlap with newInterval
        #  currInterval's start is before or equal newInterval's end
        while i < n and self.isCurrOverlapNew(intervals[i], newInterval):
            newInterval = self.mergeInterval(intervals[i], newInterval)
            i += 1

        # add the merged newInterval
        ans.append(newInterval)

        # add all intervals that come after newInterval
        ans.extend(intervals[i:])
        
        return ans
    
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            currInterval = intervals[i]
            if self.isCurrBeforeNew(currInterval, newInterval):
                ans.append(currInterval)
            elif self.isCurrOverlapNew(currInterval, newInterval):
                newInterval = self.mergeInterval(intervals[i], newInterval)
            else:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans     

        # if we reach here it means we have never added newInterval
        # AND
        # the newInterval is at the absolute end of the intervals
        ans.append(newInterval)
        return ans

soln = Solution()

assert soln.insert1([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert soln.insert1([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert soln.insert1([],[5,7]) == [[5, 7]]
assert soln.insert1([[1,5]],[6,8]) == [[1,5],[6,8]]
assert soln.insert1([[1,5]],[0,0]) == [[0, 0], [1, 5]]

assert soln.insert2([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert soln.insert2([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert soln.insert2([],[5,7]) == [[5, 7]]
assert soln.insert2([[1,5]],[6,8]) == [[1,5],[6,8]]
assert soln.insert2([[1,5]],[0,0]) == [[0, 0], [1, 5]]







