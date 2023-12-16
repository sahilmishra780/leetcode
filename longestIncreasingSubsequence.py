from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # TC: O(n^2)
        n = len(nums)
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
    
assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

# There's an alternate solution with TC: n log n
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/