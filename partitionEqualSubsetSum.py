from typing import *

class Solution:
    def canPartitionMemo(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        # now the game becomes to find a subset that sums to k
        k = sum(nums) // 2
        n = len(nums)
        memo = [[None] * (k+1) for _ in range(n)]
        def dfs(i, curr):
            if curr == 0:
                return True
            if i == n:
                return False
            if memo[i][curr] != None:
                return memo[i][curr]
            if dfs(i+1, curr - nums[i]):
                memo[i][curr] = True
                return True
            if dfs(i+1, curr):
                memo[i][curr] = True
                return True
            memo[i][curr] = False
            return False
        return dfs(0, k)
    
    def canPartitionDp(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        # now the game becomes to find a subset that sums to k
        k = sum(nums) // 2
        n = len(nums)
        memo = [[False] * (k+1) for _ in range(n + 1)]
        for i in range(n + 1):
            memo[i][0] = True
        
        for i in range(n - 1, -1 , -1):
            for curr in range(1, k + 1):
                if nums[i] <= curr and memo[i + 1][curr - nums[i]]:
                    memo[i][curr] =  True
                if memo[i + 1][curr]:
                    memo[i][curr] =  True
        return memo[0][k]

    def canPartitionDpHashset(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        # now the game becomes to find a subset that sums to k
        k = sum(nums) // 2
        n = len(nums)
        dp = set([0])

        for val in nums:
            nextDp = set()
            for t in dp:
                if t == k or val + t == k:
                    return True
                nextDp.add(t)
                nextDp.add(val + t)
            dp = nextDp
        
        return False
    
assert Solution().canPartitionMemo([1,5,11,5]) == True
assert Solution().canPartitionMemo([1,2,3,5]) == False
assert Solution().canPartitionMemo([1,2,5]) == False
assert Solution().canPartitionMemo([100]) == False

assert Solution().canPartitionDp([1,5,11,5]) == True
assert Solution().canPartitionDp([1,2,3,5]) == False
assert Solution().canPartitionDp([1,2,5]) == False
assert Solution().canPartitionDp([100]) == False

assert Solution().canPartitionDpHashset([1,5,11,5]) == True
assert Solution().canPartitionDpHashset([1,2,3,5]) == False
assert Solution().canPartitionDpHashset([1,2,5]) == False
assert Solution().canPartitionDpHashset([100]) == False
print("Success")