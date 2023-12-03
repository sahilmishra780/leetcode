from typing import *
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        - Create two arrays pac and atl indicating what positions can flow into pacific and atlantic ocean respectively
        - Start from each cell in top row and bottomrow and bfs/dfs to find all cells that can flow into pacific or atlantic ocean respectively
        - Start from each cell in left col and right row and bfs/dfs to find all cells that can flow into pacific or atlantic ocean respectively 
        - Iterate over all cells. If a cell can flow into pac and atl then add the pos to the result
        """
        M, N = len(heights), len(heights[0])
        def dfs(m, n, prev, visited):
            if (
                    m < 0 or 
                    n < 0 or 
                    m >= M or 
                    n >= N or 
                    (m, n) in visited or
                    heights[m][n] < prev
                ):
                return
            visited.add((m, n))
            dfs(m + 1, n, heights[m][n], visited)
            dfs(m - 1, n, heights[m][n], visited)
            dfs(m, n + 1, heights[m][n], visited)
            dfs(m, n - 1, heights[m][n], visited)
        
        # all cells that can reach pacific
        pac = set()
        for c in range(N):
            dfs(0, c, float('-inf'), pac)
        for r in range(M):
            dfs(r, 0, float('-inf'), pac)

        # all cells that can reach atlantic
        atl = set()
        for c in range(N):
            dfs(M-1, c, float('-inf'), atl)
        for r in range(M):
            dfs(r, N-1, float('-inf'), atl)
        
        ans = []
        for m, n in atl:
            if (m, n) in pac:
                ans.append([m, n])
        return ans