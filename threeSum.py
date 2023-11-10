class Solution:

    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i, val in enumerate(nums):
            # Invariant: Triplet val, nums[left], nums[right] should 
            # be unique
            if i > 0 and val == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ans

print(Solution().threeSum([-2,0,0,2,2]))