class Solution:
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(m, n):
            if m < 0 or m >= M or n < 0 or n >= N:
                return
            c = grid[m][n]
            if c == "0":
                return
            grid[m][n] = "0"
            for x, y in directions:
                dfs(m + x, n + y)
        count = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count
    
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(m, n):
            q = deque([[m, n]])
            grid[m][n] = "0"
            while q:
                r, c = q.popleft()
                for x, y in directions:
                    rr = r + x
                    cc = c + y
                    if rr >= 0 and rr < M and cc >= 0 and cc < N and grid[rr][cc] != "0":
                        q.append([rr, cc])
                        grid[rr][cc] = "0"
        
        count = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        return self.numIslandsDFS(grid)