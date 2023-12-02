from typing import *
from collections import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self):
        ans = [node.val for node in self.neighbors]
        return str(self.val) + "->" + str(ans)

    def __repr__(self):
        return str(self)

class Solution:
    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque([node])
        clones = {node.val: Node(node.val)}
        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n.val not in clones:
                    q.append(n)
                    clones[n.val] = Node(n.val)
                clones[curr.val].neighbors.append(clones[n.val])
        return clones[node.val]
    
    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}
        def dfs(node):
            val = node.val
            if val in clones:
                return clones[val]
            
            copy = Node(val)
            clones[val] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.cloneGraphDFS(node)
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# [[2,4],[1,3],[2,4],[1,3]]
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print(Solution().cloneGraph(node1))