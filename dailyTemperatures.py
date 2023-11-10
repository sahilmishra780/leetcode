class Solution:
    def dailyTemperatures(self, t):
        s = []
        ans = [0] * len(t)
        for i in range(len(t)):
            while s and t[s[-1][1]] <= t[i]:
                val, idx = s.pop()
                ans[idx] = i - idx
            s.append([t[i], i])
        return ans

Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70])    