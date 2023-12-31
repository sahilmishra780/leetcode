from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i, subset):
            if i == len(nums):
                ans.append(subset)
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
        dfs(0,[])
        return ans

Solution().subsets([1,2,3])