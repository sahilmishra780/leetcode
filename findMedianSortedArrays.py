class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        # Ensure A has fewer or equal elements as B
        if len(B) < len(A):
            A, B  = B, A
        total = len(A) + len(B) # Total length of merged array of A and B elements
        half = total // 2 
        """
        If total is odd, median element will have "half" elements to the left 
        and "half" elements to right. 
        If total is evem, the median will be formed by (Merged_Array[half-1] + Merged_Array[half]) / 2
        """
        
        # Binary search on A which always has length <= B
        l, r  = 0, len(A) - 1
        INT_MIN, INT_MAX = float('-inf'), float('inf')
        
        """
        len_A_left_part indicates the sub-length of elements to take from A, A[0:len_A_left_part], 
        to form the left part of the merged sorted array
        """
        len_A_left_part = INT_MAX 
        while len_A_left_part >= 0: # While we can still take elements from A
            i = l + (r - l) // 2
            len_A_left_part = i + 1
            len_B_left_part  = half - len_A_left_part
            j = len_B_left_part - 1
            
            """
            In each iteration the left part of the sorted Array is to be made of elements 
            A[0:len_A_left_part] i.e A[0:(i+1)]
            and
            B[0:len_B_left_part] i.e. A[0:(j+1)]
            """

            A_left = A[i] if i >= 0 else INT_MIN
            A_right = A[i+1] if (i + 1) < len(A) else INT_MAX
            B_left = B[j] if j >= 0 else INT_MIN
            B_right = B[j+1] if (j + 1) < len(B) else INT_MAX

            if A_left <= B_right and B_left <= A_right:
                # valid partition
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right))/2
            elif A_left > B_right:
                # Shrink partition in A
                r = i - 1
            else: # A_right < B_left
                # Expand partition in A
                l = i + 1
        return -1
print(Solution().findMedianSortedArrays([1,2,3,4,5], [1,2,3,4,5,6,7,8])) # odd
print(Solution().findMedianSortedArrays([1,2,3,4,5], [1,2,3,4,5,6,7])) # even