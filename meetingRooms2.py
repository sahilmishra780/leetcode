from typing import (
    List,
)

import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
Method: Priority Queue

We cannot process the given meetings in arbitrary order. 
The most basic way to handle meetings is to sort them in order of their start times, and that's the order we will follow. 
After all, before worrying about the 5:00 PM meeting, you should certainly schedule the 9:00 AM meeting first, right?

Algorithm:
    Sort meetings based on their start times.
    Initialize a new min heap and add the end time of the first meeting to the heap. 
    We only need to keep track of the end times in a min heap, which tells us when the room will be available.
    For each meeting, check if the minimum element in the heap (i.e., the top of the heap).
        If the room is available, remove the element from the top of the heap, update it with the end time of the current meeting, and add it back to the heap.
            This indicates that a previous meeting ended at (or before) current start time and the room is free. 
            Updating the end time is eqivalent of starting a new meeting from the same room.
        If the room is not available, open a new room and add it to the heap.
            This indicates that no previous meeting has ended at current start time. We need to start a new room.
    After processing all meetings, the size of the heap is the number of rooms required. This is the minimum number of rooms needed to accommodate these meetings.
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda interval: interval.start)
        h = []
        heapq.heappush(h, intervals[0].end)
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            if currStart >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, currEnd)
        return len(h)

intervals = [(567707,730827),(166232,719216),(634677,756013),(285191,729059),(237939,915914),(201296,789707),(578258,585240),(164298,218749),(37396,968315),(666722,934674),(742749,824917),(141115,417022),(312269,400232),(119183,598077),(48359,662082),(275411,998607),(732520,813383)]
assert Solution().min_meeting_rooms([Interval(start, end) for start, end in intervals]) == 10

intervals = [(0,30),(5,10),(15,20)]
assert Solution().min_meeting_rooms([Interval(start, end) for start, end in intervals]) == 2