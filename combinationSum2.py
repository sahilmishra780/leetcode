from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def bt(currSum, cands, pos):
            if currSum == target:
                ans.append(cands.copy())
                return
            if currSum > target:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                val = candidates[i]
                if val == prev:
                    continue
                cands.append(val)
                bt(currSum + val, cands, i + 1)
                cands.pop()
                prev = val
        bt(0, [], 0)
        return ans
Solution().combinationSum2([10,1,2,7,6,1,5], 8)