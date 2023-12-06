from typing import *
from collections import *

class Solution:
    def findOrderKahn(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build adjacency list
        # Key: a course
        # Value: list of courses that have pre-req course Key
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
        
        ans = []
        while q:
            crs = q.popleft()
            ans.append(crs)
            for nei in adj[crs]:
                # decrement indegree as crs is now completed
                indegree[nei] -=  1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ans if len(ans) == numCourses else [] # can all courses be  completed?
    
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build adjacency list
        # Key: a course
        # Value: list of courses that have pre-req course Key
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        path = set()
        completedCourses = set()
        ans = []

        def dfs(course):
            if course in completedCourses:
                return True
            if course in path:
                return False
            path.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            path.remove(course)
            completedCourses.add(course)
            ans.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
    
        return ans[::-1]
    
print(Solution().findOrderDFS(4, [[1,0],[2,0],[3,1],[3,2]]))
