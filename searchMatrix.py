class Solution:
    def searchRow(self, a, t):
        l, r = 0, len(a) - 1
        while l <= r:
            m = l + (r - l) // 2
            if a[m] == t:
                return True
            elif a[m] < t:
                r = m - 1
            else: 
                l = m + 1
        return False
    def searchMatrix(self, a, t):
        l, r = 0, len(a) - 1
        while l <= r:
            m = l + (r - l) // 2
            if a[m][0] == t:
                return True
            elif a[m][0] < t:
                r = m - 1
            else: 
                l = m + 1
        ans = False
        if l >= 0 and l < len(a):
            ans = ans or self.searchRow(a[l], t)
        if r >= 0 and r < len(a):
            ans = ans or self.searchRow(a[r], t)
        return ans
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))