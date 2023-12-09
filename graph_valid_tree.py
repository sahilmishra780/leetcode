from typing import List
from collections import defaultdict

class Solution:
    
    """
    """
    def valid_tree_vanilla(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                # there should be no cylce
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        # there should be no cylce and all n nodes must be visited
        return dfs(0, -1) and len(visited) == n

    """
    Graph Theory:
    - A graph, G is a tree, if an aonly if, the following two conditions are met:
        1.  G is fully connected. In other words, for every pair of nodes in `G`, 
            there is a path between them.
        2.  G contains no cycles. In other words, there is exactly one path between each 
            pair of nodes in G.
    - For the graph to be a valid tree, it must have _exactly n - 1 edges. 
        Any less, and it can't possibly be fully connected. 
        Any more, and it has to contain cycles. Additionally, if the graph is 
        fully connected and contains exactly n - 1 edges, it can't possibly 
        contain a cycle, and therefore must be a tree!
    """
    def valid_tree_union_find(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return  False

        par = [i for i in range(n)]
        rank = [1] * n

        count = n
        def find(x):
            while x != par[x]:
                x = par[x]
            return x
        
        def union(x1, x2):
            nonlocal count
            p1, p2 = find(x1), find(x2)

            if p1 == p2:
                return 
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            count -=1

        for x, y in edges:
            union(x, y)
        
        return count == 1
    
    def valid_tree_dfs(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: 
            return  False

        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
        
        dfs(0, -1)
        
        return len(visited) == n

print(Solution().valid_tree_vanilla(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().valid_tree_vanilla(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(Solution().valid_tree_union_find(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().valid_tree_union_find(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(Solution().valid_tree_dfs(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().valid_tree_dfs(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))