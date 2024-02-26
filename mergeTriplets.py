from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        """
        target = (x, y, z)
        We only care about a triplet (a, b, c) if a <= x and b <= y and c <= z
        So step 1 is to clean the input triplets such that all triplets (a, b, c)
        satisfy the invariant (a, b, c)  i.e. a <= x and b <= y and c <= z

        Now, the solution will only exist if we have atleast 1 triplet that has the
        target triplet element matching at the corresponding index. So we need to 
        have 
        1.  atleast one triplet (a, -, -) s.t. a = x, 
        2.  atleast one triplet (-, b, -) s.t. b = y, 
        3.  atleast one triplet (-, -, c) s.t. c = z

        If the above two conditions are met then return True  
        """
        x, y, z = target
        st = set()
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                st.add(tuple([a, b, c]))
        
        isPresent = [False] * 3
        for a, b, c in st:
            if x == a:
                isPresent[0] = True
            if y == b:
                isPresent[1] = True
            if z == c:
                isPresent[2] = True
        
        return isPresent[0] and isPresent[1] and isPresent[2]
    

soln = Solution()
assert soln.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]) == True
assert soln.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]) == True
assert soln.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]) == False
assert soln.mergeTriplets([[3,5,1],[10,5,7]], [3,5,7]) == False