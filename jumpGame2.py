from typing import List

class Solution:
    def jumpMemoized(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(i):
            if i >= n - 1:
                return 0
            maxSteps = nums[i]
            if memo[i] != -1:
                return memo[i]
            memo[i] = float('inf')
            for idx in range(maxSteps, 0, -1):
                memo[i] = min(1 + dp(i + idx), memo[i])
            return memo[i]
        return dp(0)

    def jumpDp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n-2, -1, -1):
            maxSteps = nums[i]
            dp[i] = float('inf')
            for step in range(maxSteps, 0, -1):
                idx = i + step
                if idx >= n:
                    dp[i] = 1
                    break
                dp[i] = min(dp[i], 1 + dp[idx])
        return dp[0]
    
    """
    Let's say the range of the current jump is [left, right] and furthest is the
    furthest point that all points in [left, right] can reach. 
    To determine the furthest point go over all i s.t left <= i <= right and find the 
    furthest point that we can reach by furthest = max(furthest, i + nums[i])
    Once the furthest point reachable from [left, right] is determined, update the
    new right to point to the furthest point and the new left to point to the index
    just after the previous right. This update indicates a jump and therefore we
    increment the steps taken by 1. This is like a BFS level increment.
    Terminate the BFS once the new right is >= n - 1
    """
    def jumpGreedy(self, nums: List[int]) -> int:
        steps = 0
        left, right = 0, 0 # defines the window
        while right < len(nums) - 1:
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            left = right + 1
            right = furthest
            steps += 1
        return steps
soln = Solution()
assert soln.jumpMemoized([2,3,1,1,4]) == 2
assert soln.jumpMemoized([2,3,0,1,4]) == 2

assert soln.jumpDp([2,3,1,1,4]) == 2
assert soln.jumpDp([2,3,0,1,4]) == 2

assert soln.jumpGreedy([2,3,1,1,4]) == 2
assert soln.jumpGreedy([2,3,0,1,4]) == 2
assert soln.jumpGreedy([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]) == 5
