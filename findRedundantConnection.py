from collections import *
from typing import *

class Solution:
    def findRedundantConnectionDFS(self, edges: List[List[int]]) -> List[int]:
        
        # build bi-directied adjacency list
        adj = defaultdict(list)
        for node, connection in edges:
            adj[node].append(connection)
            adj[connection].append(node)
        
        cycle = {} # dict preserves order of insertion
        def dfs(node, parent):
            if node in cycle:
                # once we find cycle we want to only keep nodes that form the cycle
                # delete all nodes before the start of the cycle
                for k in list(cycle.keys()):
                    if k == node:
                        return True # cycle present
                    del cycle[k]   
            cycle[node] = None
            for child in adj[node]:
                if child != parent and dfs(child, node):
                    return True # cycle present
            # no cycle can be formed starting from node
            del cycle[node] # delete node as no cycle can be formed
            return False # no cycle formed
            
        dfs(edges[0][0],-1)
        for a,b in edges[::-1]:
            if a in cycle and b in cycle:
                return (a,b)
    
    def findRedundantConnectionUnionFind(self, edges: List[List[int]]) -> List[int]:
        """
        Note that having n nodes and n edges will always result in a cycle
        
        Union-Find implementation:
        1. Parent array of size N with values 1,2,..., N indicating that parent[i] = i (1-based index) 
           i.e. initially we have N distinct components
        2. As we have N distinct components initially, we initialize a rank array of size N with all values 1
           Rank indicates the number of elements in a component. Higher rank larger number of elements in a component 
        3. Always add the smaller component (lower rank) to the larger component (higher rank). 
           If components are of same size (equal rank) then add the second component to be the child of the first component
           Union logic for n1 and n2
            a. p1 -> parent of n1, p2 -> parent of n2
            b. if rank[p1] > rank[p2], make p2's parent as p1, update rank[p1] += rank[p2]
            c. else make p1's parent as p2, update rank[p2] += rank[p1]
        4. For the union operation return True to indicate if we unionized 2 components, if the currnet union was merging
           2 already merged components (i.e current edge was redundant) return False
        5. For find operation (operation that finds the root of a node n) we need to find node p s.t. par[p] == p
        5. (Optional) Obviosly Step 5, requires a while loop with exit condition par[p] != p. To add path compression, make every node
           point to its grandparent.

        Main function:
        1. Go over all edges and k
        """
        n = len(edges)
        par = [i for i in range(n+1)] # 0, 1, ...n (0 is ignored)
        rank = [1] * (n + 1)

        def find(n):
            while par[n] != n:
                """
                Optimization: path compression
                node = n
                parent = par[node]
                grandparent = par[parent]
                par[node] = grandparent
                OR, in a single line
                par[n] = par[par[n]]
                """
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False # we found the redundant edge (n1, n2), return False to indicate operation failure
            
            if rank[p1] > rank[p2]:
                # make p1 the parent of p2
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                # make p2 the parent of p1
                par[p1] = p2
                rank[p2] += rank[p1]
            return True # return True to indicate operation success

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

# ans = Solution().findRedundantConnectionDFS([[1,4],[1,2],[2,3],[3,4],[1,5]])
ans = Solution().findRedundantConnectionUnionFind([[1,4],[1,2],[2,3],[3,4],[1,5]])
print(ans)