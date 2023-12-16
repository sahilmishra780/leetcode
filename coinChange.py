from typing import List

class Solution:
    def coinChangeMemo(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        def dp(currSum):
            if currSum == 0:
                return 0
            if currSum < 0:
                return float('inf')
            if memo[currSum] != -1:
                return memo[currSum]
            
            ans = float('inf')
            for coin in coins:
                ans = min(ans, 1 + dp(currSum - coin))
            memo[currSum] = ans
            return memo[currSum]
        
        res = dp(amount)
        return -1 if res == float('inf') else res
    
    def coinChangeDp(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for currSum in range(1, amount + 1):
            for coin in coins:
                if currSum - coin >= 0:
                    dp[currSum] = min(dp[currSum], 1 + dp[currSum - coin])
        
        return -1 if dp[amount] == float('inf') else dp[amount]
    
print(Solution().coinChangeMemo([1, 2, 5], 11))
print(Solution().coinChangeDp([1, 2, 5], 11))