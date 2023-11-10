class Solution:
    def findMin(self, a):
        l, r = 0, len(a) - 1
        ans = -5001
        while l <= r:
            m = l + (r - l) // 2
            if a[m] > a[r]:
                l = m + 1
            else:
                ans = a[m]
                r = m - 1
        return ans
Solution().findMin([3,1,2])