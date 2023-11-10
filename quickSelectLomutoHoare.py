class Solution:
    # Hoare partition is faster than Lomuto's partition
    def hoarePartition(self, nums, left, right):
        # randomize pivot for better performance
        pivot = nums[right]
        i, j = left, right - 1
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[right], nums[i] = nums[i], nums[right]
        return i
    
    def hoarePartition2(self, nums, left, right):
        pivot = nums[left]
        i, j = left + 1, right
        while True:
            while i < j and nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j
    
    def lomutoPartition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill
    
    def quickSelect(self, nums, left, right, k):
        if left == right:
            return nums[left]
        p = self.hoarePartition(nums, left, right)
        if p > k:
            return self.quickSelect(nums, left, p - 1, k)
        elif p < k:
            return self.quickSelect(nums, p + 1, right, k)
        return nums[k]
    
    def findKthLargest(self, nums, k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
        

print(Solution().findKthLargest([3,2,1,5,6,4], 2))