class Solution:
    
    def climbStairsMemo(self, n: int, mp = {}) -> int:
        if n < 0:
            return 0
        if n == 1 or n == 0:
            return 1
        if n in mp:
            return mp[n]
        mp[n] = self.climbStairsMemo(n - 1) + self.climbStairsMemo(n - 2) 
        return mp[n]
           
    def climbStairsDP(self, n: int) -> int:
        mp = [0] * (n + 1)
        mp[0], mp[1] = 1, 1
        for i in range(2, n+1):
            mp[i] = mp[i - 1] + mp[i - 2]
        return mp[n]

print(Solution().climbStairsMemo(18))
print(Solution().climbStairsDP(18))