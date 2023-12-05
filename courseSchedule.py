from typing import *
from collections import *

class Solution:
    def canFinishKahn(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Kahn's topological sort
        """ 

        # build adjacency list
        adj = defaultdict(list)

        # indegree represents num of prereqs for a particular course
        # indegree = 0 indicates course with no prereqs
        # visually it is the number of incoming arrows into a node
        # once we complete a prereq we can decrement indegree
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0: # course with no prereq
                q.append(i)
        count = 0
        while q:
            crs = q.popleft()
            count += 1 # increment count as crs is now completed
            for nei in adj[crs]:
                # decrement indegree as crs is now completed
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return numCourses == count # can all courses be  completed?

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        path = set()
        canComplete = set()
        def dfs(i):
            if i in path:
                return False
            if i in canComplete:
                return True
            path.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            path.remove(i)
            canComplete.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True