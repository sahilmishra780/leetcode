from typing import List

class Solution:
    def minCostClimbingStairs0(self, cost: List[int]) -> int:
        N = len(cost)
        memo = [-1] * N
        def recurse(idx):
            if idx >= N - 1:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = min(cost[idx] + recurse(idx + 1), cost[idx + 1] + recurse(idx + 2))
            return memo[idx]
        return recurse(0)

    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        N = len(cost)
        memo = [0] * (N + 1)
        for idx in range(N - 2, -1, -1):
            memo[idx] = min(cost[idx] + memo[idx + 1], cost[idx + 1] + memo[idx + 2])
        return memo[0]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        N = len(cost)
        next, afterNext = 0, 0
        for idx in range(N - 2, -1, -1):
            next, afterNext = min(cost[idx] + next, cost[idx + 1] + afterNext), next

        return next

print(Solution().minCostClimbingStairs0([1,100,1,1,1,100,1,1,100,1]))
print(Solution().minCostClimbingStairs1([1,100,1,1,1,100,1,1,100,1]))
print(Solution().minCostClimbingStairs2([1,100,1,1,1,100,1,1,100,1]))