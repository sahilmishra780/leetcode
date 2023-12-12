from typing import List

class Solution:
    def rob0(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [-1] * N
        def dp(i):
            if i >= N:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dp(i + 2), dp(i+1))
            return memo[i]
        dp(0)
        return memo[0]
    
    def rob1(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [0] * (N + 2)
        for i in range(N-1, -1, -1):
            memo[i] = max(nums[i] + memo[i + 2], memo[i+1])
        return memo[0]
    
    def rob2(self, nums: List[int]) -> int:
        N = len(nums)
        next, afterNext = 0, 0
        for i in range(N-1, -1, -1):
            next, afterNext = max(nums[i] + afterNext, next), next
        return next

    def rob3(self, nums: List[int]) -> int:
        N = len(nums)
        next, afterNext = 0, 0
        for i in range(N-1, -1, -1):
            next, afterNext = max(nums[i] + afterNext, next), next
        return next    

print(Solution().rob0([2,7,9,3,1]))
print(Solution().rob1([2,7,9,3,1]))
print(Solution().rob2([2,7,9,3,1]))
print(Solution().rob3([2,7,9,3,1]))