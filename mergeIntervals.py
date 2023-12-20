from typing import List

class Solution:
    def mergeIntuition(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevInterval = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            prevStart, prevEnd = prevInterval
            if newStart <= prevEnd:
                prevStart = min(prevStart, newStart)
                prevEnd = max(prevEnd, newEnd)
                prevInterval = [prevStart, prevEnd]
            else:
                ans.append(prevInterval)
                prevInterval = intervals[i]
        ans.append(prevInterval)
        return ans
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):  
            start, end = intervals[i]
            prevEnd = ans[-1][1]
            if start <= prevEnd:
                # merge
                ans[-1][1] = max(prevEnd, end)
            else:
                # add interval
                ans.append(intervals[i])
        return ans

soln = Solution()

assert soln.mergeIntuition([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert soln.mergeIntuition([[1,4],[4,5]]) == [[1,5]]

assert soln.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert soln.merge([[1,4],[4,5]]) == [[1,5]]