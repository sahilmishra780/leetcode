from typing import List
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """ 
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        M, N = len(rooms), len(rooms[0])
        INF = 2147483647
        q = deque()
        
        # populate all gates in q
        for r in range(M):
            for c in range(N):
                if rooms[r][c] == 0:
                    q.append((r,c))
        
        # helper function to add a new room to q
        # and add its distance from its nearest gate
        def addRoom(m, n, dist):
            """
            rooms[m][n] can be 
            1. 0 -> gate (don't proceed because gate)
            2. -1 -> wall (don't proceed because gate)
            3. value s.t. 0 < value < INF (dist was already written in prev iteration)
            """
            if (
                m < 0 or
                n < 0 or
                m == M or
                n == N or
                rooms[m][n] != INF 
                ):
                return
            q.append((m, n))
            rooms[m][n] = dist

        # the first room from the gate will have a dist of 1
        dist = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                m, n = q.popleft()
                addRoom(m + 1, n, dist)
                addRoom(m - 1, n, dist)
                addRoom(m , n + 1, dist)
                addRoom(m, n - 1, dist)
            dist += 1

room = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Solution().walls_and_gates(room)
for row in room: print(row)