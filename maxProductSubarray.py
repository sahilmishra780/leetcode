from typing import *

class Solution:
    """
    Hint: Kadane's algorithm
    Observe that negative values can produce the maximum product, 
    we keep track of both maximum product and the minimum product. 
    The minimum product, when multiplied by another negative number, 
    can produce a possible answer. 
    """
    def maxProductDP(self, nums: List[int]) -> int:
        n = len(nums)
        minProd = [1] * n
        maxProd = [1] * n
        ans = minProd[0] = maxProd[0] = nums[0]
        for i in range(1, n):
            val = nums[i]
            maxProd[i] = max(val, minProd[i-1] * val, maxProd[i-1] * val)
            minProd[i] = min(val, minProd[i-1] * val, maxProd[i-1] * val)
            ans = max(ans, maxProd[i])
        return ans
    
    def maxProductConstantSpace(self, nums: List[int]) -> int:
        n = len(nums)
        prevMinProd, prevMaxProd, ans = 1, 1, float('-inf')
        for val in nums:
            currMaxProd = max(val, prevMinProd * val, prevMaxProd * val)
            currMinProd = min(val, prevMinProd * val, prevMaxProd * val)
            prevMinProd, prevMaxProd = currMinProd, currMaxProd
            ans = max(ans, currMaxProd)
        return ans

print(Solution().maxProductDP([2,3,-2,4]))
print(Solution().maxProductDP([-2,0,-1]))
print()
print(Solution().maxProductConstantSpace([2,3,-2,4]))
print(Solution().maxProductConstantSpace([-2,0,-1]))