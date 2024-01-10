from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = float('-inf')
        for val in nums:
            currSum += val
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum
    
soln = Solution()
assert soln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert soln.maxSubArray([1]) == 1
assert soln.maxSubArray([5,4,-1,7,8]) == 23