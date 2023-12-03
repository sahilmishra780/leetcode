from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        think of it this way
        You want to return the boards with only thos O's that have
        a path to the boundary. These O's cannot be captured as they
        will always have an O or the boundary guarding a side

        Therefore we start dfs from any boundary "O" node and mark
        that boundary node and all reachable "O" nodes from that node 
        with a mark "T"

        Then we iterate, over the board again and check for "O"s. These
        "O"s by design would not have a path to the boundary and therefore
        can be captured

        Finally we iterate over the board and re-mark all the "T" nodes
        as "O" as these are the nodes that have a path to the boundaries
        """
        M, N = len(board), len(board[0])
        def dfs(m, n):
            if (
                m < 0 or
                m >= M or 
                n < 0 or
                n >= N or
                board[m][n] != "O"
            ):
                return
            board[m][n] = "T"
            dfs(m + 1, n)
            dfs(m - 1, n)
            dfs(m, n + 1)
            dfs(m, n - 1)

        for c in range(N):
            if board[0][c] == "O":
                dfs(0, c)
            if board[M - 1][c] == "O":
                dfs(M - 1, c)
        for r in range(M):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][N-1] == "O":
                dfs(r, N-1)
        for r in range(M):
            for c in range(N):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(M):
            for c in range(N):
                if board[r][c] == "T":
                    board[r][c] = "O"
