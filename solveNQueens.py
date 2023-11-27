from typing import *
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for i in range(n)]
        ans = []
        vert = set()
        diag = set()
        def mark(R,C):
            i = 1
            vertsAdded = []
            diagsAdded = []
            for r in range(R+1, n):
                if (r, C) not in vert:
                    vert.add((r, C))
                    vertsAdded.append((r,C))
                vert.add((r, C))
                if C - i >= 0 and (r, C - i) not in diag:
                    diag.add((r, C - i))
                    diagsAdded.append((r, C - i))
                if C + i < n and (r, C + i) not in diag:
                    diag.add((r, C + i))
                    diagsAdded.append((r, C + i))
                i += 1
            return (vertsAdded, diagsAdded)
        def unmark(vertsAdded, diagsAdded):
            for t in vertsAdded:
                vert.remove(t)
            for t in diagsAdded:
                diag.remove(t)
            
        def bt(r):
            if r == n:
                ans.append(["".join(brd) for brd in board])
                return
            for c in range(n):
                t = (r,c)
                if t in vert or t in diag:
                    continue
                board[r][c] = "Q"
                (vertsAdded, diagsAdded) = mark(r, c)
                
                bt(r+1)
                
                unmark(vertsAdded, diagsAdded)
                board[r][c] = "."

        bt(0)
        return ans
    