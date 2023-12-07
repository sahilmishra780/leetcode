from typing import *
class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        par = [i for i in range(n)]
        rank = [1] * (n)
        count = n
        def find(n):
            while par[n] != n:
                n = par[n]
            return n

        def union(n1, n2):
            nonlocal count
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            count -= 1
        
        for n1, n2 in edges:
            union(n1, n2)
        
        return count
    
print(Solution().count_components(3, [[0,1], [0,2]]))
print(Solution().count_components(6, [[0,1], [1,2], [2, 3], [4, 5]]))