from typing import *
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for i in range(n)]
        ans = []
        cols = set()
        sumDiag = set() # down left diagonal, Here r + c remains constant
        diffDiag = set() # down right diagonal, Here r - c remains constant

        def bt(r):
            if r == n:
                ans.append(["".join(brd) for brd in board])
                return
            for c in range(n):
                if c in cols or (r + c) in sumDiag or (r - c) in diffDiag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                sumDiag.add(r+c)
                diffDiag.add(r-c)
                
                bt(r+1)
                
                cols.remove(c)
                sumDiag.remove(r+c)
                diffDiag.remove(r-c)
                board[r][c] = "."

        bt(0)
        return ans
    