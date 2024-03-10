from typing import List
from collections import defaultdict

class Solution:
    def findItineraryBacktracking(self, tickets: List[List[str]]) -> List[str]:
        """
        - Start node is JFK
        - Atleast 1 valid itinerary
        - Use all tickets exactly once. So not allowed to go over the same edge
          multiple times. But allowed to go over the same node multiple times
        - If multiple solutions, return in lexical order
        """

        """
        1. Create an adjacency list using key as source and value
           as list of of destinations from that source. Make the value 
           a sorted list so that we always visit the destinations in 
           lexical order and therefore in the case of multiple valid itineraries 
           return the itinerary with the smaller lexical order. To ensure this 
           invariant of keeping the value list sorted, sort the input list and then 
           build the adjacency list
        2. DFS and try to complete the path. How do we know if the itinerary
           valid? -> Len of output == len(tickets) + 1(for JFK)
           Explanation: Visiting each ticket causes 1 value to be added to the
           output and we always add the start point JFK to the output
        """
        
        # sort tickets so that we build the itinerary in lexical order
        tickets.sort()
        
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        # visited map to indicate if we have visited 
        # the ticket pointed by [src] -> dst = adj[src][i]
        visited = {}
        for src, dstlist in adj.items():
            # note dstlist is always lexically sorted
            visited[src] = [False] * len(dstlist)
        
        res = ["JFK"]
        def dfs(src):
            # How do we know if the itinerary valid? 
            # -> Len of output == len(tickets) + 1(for JFK)
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            for i, v in enumerate(adj[src]):
                # don't visit a src->dest pair that has been visited before
                if not visited[src][i]:
                    visited[src][i] = True
                    res.append(v)
                    if dfs(v): 
                        return True
                    visited[src][i] = False
                    res.pop()
            return False
        dfs("JFK")
        return res
    
    """
    See notes in eulerianPathAndCircuit.md
    """
    def findItineraryEulerianPath(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        

        adj = defaultdict(list)    
        for src, dst in tickets:
            adj[src].append(dst)

        ans = []
        def dfs(at):
            while adj[at]:
                dst = adj[at].pop()
                dfs(dst)
            ans.append(at)
        
        dfs("JFK")
        return ans[::-1]

soln = Solution()
assert soln.findItineraryBacktracking(
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    ) == ["JFK","MUC","LHR","SFO","SJC"]
assert soln.findItineraryBacktracking(
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    ) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
assert soln.findItineraryEulerianPath(
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    ) == ["JFK","MUC","LHR","SFO","SJC"]
assert soln.findItineraryEulerianPath(
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    ) == ["JFK","ATL","JFK","SFO","ATL","SFO"]