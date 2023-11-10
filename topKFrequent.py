from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Optimization
        if k == len(nums):
            return nums
        
        freq = Counter(nums)
        A = list(freq.keys())
        def partition(l, r):
            pivot = freq[A[r]]
            p = l
            for i in range(l, r):
                if freq[A[i]] < pivot:
                    A[p], A[i] = A[i], A[p]
                    p += 1
            A[p], A[r] = A[r], A[p]
            return p
        
        def quickSelect(l, r, k_smallest):
            if l == r:
                return
            p = partition(l, r)
            if p < k_smallest:
                quickSelect(p + 1, r, k_smallest)
            elif p > k_smallest:
                quickSelect(l, p - 1, k_smallest)
        
        quickSelect(0, len(A) - 1, len(A) - k)
        
        return A[len(A) - k:]