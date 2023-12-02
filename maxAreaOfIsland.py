from typing import *
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [[1,0], [-1, 0], [0, -1], [0, 1]]
        def dfs(m, n):
            if m < 0 or m >= M or n < 0 or n >= N or grid[m][n] == 0:
                return 0
            area = 1
            grid[m][n] = 0
            for x, y in dirs:
                area += dfs(m + x, n + y)
            return area
        maxArea = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:                    
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea   
    

print(Solution().maxAreaOfIsland(
        [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
    )
)