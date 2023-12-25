from typing import List

class Interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda interval: interval.end)
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            if currStart < prevEnd:
                return False
            else:
                prevEnd = currEnd
        return True
    
soln = Solution()
assert soln.can_attend_meetings([Interval(0,30),Interval(5,10),Interval(15,20)]) == False
assert soln.can_attend_meetings([Interval(5,8),Interval(9,15)]) == True
