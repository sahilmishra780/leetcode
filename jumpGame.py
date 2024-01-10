from typing import List

class Solution:
    def canJumpMemoized(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [None] * n
        def dp(i):
            if i >= n - 1:
                return True
            if memo[i] != None:
                return memo[i]
            maxSteps = nums[i]
            for idx in range(maxSteps, 0, -1):
                if dp(i + idx):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dp(0)
    
    def canJumpDp(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            maxSteps = nums[i]
            for step in range(maxSteps, 0, -1):
                idx = i + step
                if idx >= n:
                    dp[i] = True
                else:
                    dp[i] = dp[idx]
                if dp[i]:
                    break
        return dp[0]
    
    """
    Greedy Solution:
    use a variable to hold the furthest point we can reach so far, 
    ie. furthest = max(furthest, i + nums[i]). 
    We can only reach the end if at the end of going over all the elements
    in the array we have furthest >= n - 1
    There's one catch, if at any index i, the value of furthest < i this means
    that we can never reach that position from and index before it e.g [3, 2, 1, 0, 4]
    """
    def canJumpGreedy(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)):
            if furthest < i:
                return False
            furthest = max(furthest, i + nums[i])
        return furthest >= len(nums) - 1

soln = Solution()

assert soln.canJumpMemoized([2,3,1,1,4]) == True
assert soln.canJumpMemoized([3,2,1,0,4]) == False
assert soln.canJumpMemoized([2,5,0,0]) == True

assert soln.canJumpDp([2,3,1,1,4]) == True
assert soln.canJumpDp([3,2,1,0,4]) == False
assert soln.canJumpDp([2,5,0,0]) == True

assert soln.canJumpGreedy([2,3,1,1,4]) == True
assert soln.canJumpGreedy([3,2,1,0,4]) == False
assert soln.canJumpGreedy([2,5,0,0]) == True

