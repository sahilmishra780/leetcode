from typing import *
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        
        def bt(m, n, i):
            if i == len(word):
                return True
            c = board[m][n]
            if word[i] != c or c == "#":
                return False
            board[m][n] = "#"
            if m - 1 >= 0 and bt(m - 1, n, i + 1):
                return True
            if m + 1 < M and bt(m + 1, n, i + 1):
                return True 
            if n - 1 >= 0 and bt(m, n - 1, i + 1):
                return True 
            if n + 1 < N and bt(m, n + 1, i + 1):
                return True
            board[m][n] = c
            return False
        
        for m in range(M):
            for n in range(N):
                if board[m][n] == word[0] and bt(m, n, 0):
                    return True
        return False
        
print(Solution().exist([["a"]], "a"))