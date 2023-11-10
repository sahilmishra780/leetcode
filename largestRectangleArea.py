class Solution:
    def largestRectangleArea(self, h):
        maxArea = 0
        s = []
        n = len(h)
        for i in range(len(h)):
            curr = h[i]
            pIdx = i
            while s and s[-1][1] > curr:
                pIdx, pVal = s.pop()
                width = i - pIdx
                height = pVal
                area = height * width
                maxArea = max(maxArea, area)
            s.append([pIdx, curr])
        while s:
            pIdx, pVal = s.pop()
            width = n - pIdx
            height = pVal
            area = height * width
            maxArea = max(maxArea, area)
        return maxArea
print(Solution().largestRectangleArea([999,999,999,999]))
