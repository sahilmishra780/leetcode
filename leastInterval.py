from collections import *
from typing import *
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], idleTime: int) -> int:
        count = Counter(tasks)
        maxHeap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        str = ""
        while q or maxHeap:
            time += 1
            currTask = "idle"
            if maxHeap:
                # use 1 count from freq
                freq, currTask = heapq.heappop(maxHeap)
                freq += 1
                if freq: 
                    # i.e. there are more tasks of this type to process
                    # now append freq and time when this task
                    # will be available to use
                    q.append([freq, time + idleTime, currTask])
            if q and q[0][1] == time:
                # no char is used
                # char is still "idle"
                f, _, t = q.popleft()
                heapq.heappush(maxHeap, (f, t))
            str += currTask + "->"
        # print(str)    
        return time

Solution().leastInterval(["A","A","A","B","B","B"], 3)