from typing import *
class Solution:
    # code for house robber 1 problem
    def __houseRobber1(self, nums: List[int]) -> int:
        N = len(nums)
        next, afterNext = 0, 0
        for i in range(N-1, -1, -1):
            next, afterNext = max(nums[i] + afterNext, next), next
        return next

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.__houseRobber1(nums[:n-1]), self.__houseRobber1(nums[1:]))

print(Solution().rob([1,2,3,1]))