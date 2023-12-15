class Solution:
    def numDecodingsRecursive(self, s: str) -> int:
        """
        Recursive solution. Obviously will give TLE in Leetcode submission
        T(n): O(2^n) where 'n' is the length of the input string.

        In the worst case, the recursive function explores two possibilities at each step:
        1. Decode the current digit and the rest of the string.
        2. Decode the current and next digit together and the rest of the string

        In the worst case, at each recursive call, we make two recursive calls (except for the base cases when i == n). 
        Therefore, the number of recursive calls doubles with each level of recursion and we have to go a depth of n
        Therefore T(n) = 2^n
        """
        n = len(s)
        if n == 0:
            return 0
        
        st = set([str(i) for i in range(1,27)])
        def dp(i):
            # Base case
            if i == n:
                return 1
            # Exclude substrings that start with 0
            if s[i] == '0':
                return 0 # substring cannot start from 0
            
            res = dp(i + 1)
            if i < n - 1 and s[i:i+2] in st:
                res += dp(i + 2)
            return res
        
        return dp(0)

    def numDecodingsMemo(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        memo = [-1] * n
        st = set([str(i) for i in range(1,27)])
        def dp(i):
            # Base case
            if i == n:
                return 1
            # Exclude substrings that start with 0
            if s[i] == '0':
                return 0 # substring cannot start from 0
            
            # Memoization
            if memo[i] != -1:
                return memo[i]
            memo[i]  = dp(i + 1)
            if i < n - 1 and s[i:i+2] in st:
                memo[i] += dp(i + 2)
            return memo[i]
        
        return dp(0)
    
    def numDecodingsDP(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)
        dp[n] = 1
        st = set([str(i) for i in range(1,27)])
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] += dp[i + 1]
            if i < n - 1 and s[i:i+2] in st:
                dp[i] += dp[i + 2]
            
        return dp[0]

print(Solution().numDecodingsMemo("11106"))
print(Solution().numDecodingsMemo("12"))
print(Solution().numDecodingsMemo("226"))
print(Solution().numDecodingsMemo("06"))
print()
print(Solution().numDecodingsMemo("11106"))
print(Solution().numDecodingsMemo("12"))
print(Solution().numDecodingsMemo("226"))
print(Solution().numDecodingsMemo("06"))
print()
print(Solution().numDecodingsDP("11106"))
print(Solution().numDecodingsDP("12"))
print(Solution().numDecodingsDP("226"))
print(Solution().numDecodingsDP("06"))