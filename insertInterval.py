from typing import List
import heapq

class Solution:
    def insertIntuition(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        heapq.heapify(intervals)
        ans = []
        while intervals:
            left, right = heapq.heappop(intervals)
            while ans:
                prevLeft, prevRight = ans.pop()
                if prevLeft <= left <= prevRight or prevLeft <= right <= prevRight:
                    left = min(prevLeft, left)
                    right = max(prevRight, right)
                else:
                    ans.append([prevLeft, prevRight])
                    break
            ans.append([left, right])
        return ans

soln = Solution()

assert soln.insertIntuition([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert soln.insertIntuition([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert soln.insertIntuition([],[5,7]) == [[5, 7]]
assert soln.insertIntuition([[1,5]],[6,8]) == [[1,5],[6,8]]
assert soln.insertIntuition([[1,5]],[0,0]) == [[0, 0], [1, 5]]







