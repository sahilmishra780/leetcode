from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 2:
                    q.append((m, n))
                elif grid[m][n] == 1:
                    fresh += 1
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while fresh > 0 and q:
            sz = len(q)
            for _ in range(sz):
                m, n = q.popleft()
                for xx, yy in dirs:
                    r, c = m + xx, n + yy
                    if (
                        r in range(M) and
                        c in range(N) and
                        grid[r][c] == 1
                    ):
                        q.append((r, c))
                        fresh -= 1
                        grid[r][c] = 2
            time += 1

        return time if fresh == 0 else -1