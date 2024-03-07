## Existence of Eulerian Paths and Circuits

*[Reference](https://youtu.be/xR4sGgwtR2I?si=PX6L2kVOLx1gfXaf)*
### Introduction
Eulerian path is a path of edges that visits all the edges in a graph once. To find an eulerian path you need to start at specific nodes. Choosing the wrong start node can lead to unreachable edges. Similarly, an Eulerian Circuit is an Eulerian path which starts and ends at the same vertex. Note that every Eulerian circuit is an Eulerian path. If a graph has an Eulerian circuit then we can start at any node. If the graph does not have an Eulerian cycle then you will not be able to return to the start node or you will not be able to visit all edges.
### Node Degrees
For undirected graphs node degree is the number of edges attached to the node. For a directed graph node indegree is the number of incoming edges and node outdegree is the number of outgoing edges
### Conditions for Eulerian Path/Circuit

|                  | Eulerian Circuit                              | Eulerian Path                                                                                                                                                        |
| ---------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Undirected Graph | Every vertex has an even degree               | Either every vertex has even degree or exactly two vertices have odd degree                                                                                          |
| Directed Graph   | Every vertex has equal indegree and outdegree | At most one vertex has *(outdegree) - (indegree) = 1* and at most one vertex has *(indegree) - (outdegree) = 1* and all other vertices have equal in and out degrees |
An additional requirement when finding paths/circuits is that ***all vertices with nonzero degree*** need to belong to a ***single connected component***.

Also note that a singleton node, 0 node degree or 0 indegree and outdegree, does not impact whether there is an Eulerian cycle/path
## Eulerian Path/Circuit algorithm: Hierholzer's algorithm
*[Reference](https://youtu.be/8MpoO2zA2l4?si=cJbLc-6qBddGyFjq)*
Finding Eulerian Path/Circuit are very similar problems for both directed and undirected graphs. If we have an algorithm that finds the Eulerian Path then we just have to feed the algorithm a graph with an Eulerian Cycle and the algorithm will output the Eulerian Cycle as the Eulerian Path. 
### Finding an Eulerian Path (directed graph)
First verify that Eulerian Path exists. Recall that the condition for a directed graph to have an Eulerian Path is "every vertex has equal indegree and outdegree | At most one vertex has *(outdegree) - (indegree) = 1* and at most one vertex has *(indegree) - (outdegree) = 1* and all other vertices have equal in and out degrees". So count the indegree and outdegree of each node and verify the Eulerian path exists. The start node is usually the node with the extra outdegree and the end node is usually the node that has the extra indegree. Note that if all indegree and outdegree are equal then we have an Eulerian circuit and we can start from any node. The first line of though would be do a random DFS starting at the start node. In this case you may reach the end node via the DFS but you may not cover all edges and therefore will not find the Eulerian path. Therefore we have to force our DFS to visit all edges.
1. Start at the start node
2. Do DFS
3. Once the current node has no unvisited outgoing edges, we backtrack and add the current node to the solution
	1. We already calculated the number of outgoing edges from a node in the outdegree. While doing the DFS every time we visit an edge we'll reduce the outgoing edge count in the out array. This will enable us to know when a certain node has no more unvisited edges.
4. We do this until we reach the start node and the recursion unwinds
Time complexity: O(E). The calculations we're doing: computing in/out degrees and the dfs are linear in the number of edges.
### Pseudocode
```python
# Global/class scope variables
n = number of vertices in the graph
m = number of edges in the graph

in = [0] * n # Length n
out = [0] * n # Length n

path = linked-list

def countInOutDegrees():
	for edges in g:
		for edge in edges:
			out[edge.from] += 1
			in[edge.to] += 1

def graphHasEulerianPath():
	start_nodes, end_nodes = 0, 0
	for i in range(n):
		if out[i] - in[i] > 1 or in[i] - out[i] > 1:
			return False
		elif out[i] - in[i] == 1:
			start_nodes += 1
		elif in[i] - out[i] == 1:
			end_nodes += 1
	return (end_nodes == 0 and start_nodes == 0) or 
			(end_nodes == 1 and start_nodes == 1)

"""
finds the start node for a graph that is known to have an Eulerian Path
"""
def findStartNode():
	start = 0
	for i in range(n):
		# unique starting node
		if out[i] - in[i] == 1: return i
		# start at any node with an outgoing edge
		if out[i] > 0: start = i
	return start

def dfs(at):
	# While the current node still has outgoing edges
	while out[at] != 0:

		"""
		Here the out array serves two purposes. One is to track 
		whether or not there are still unvisited outgoing edges and 
		the other is to index into the adj klist to select the next
		outgoing edge
		"""
		# Decrement the number of outgoing edges from 
		out[at] -= 1
		
		# Select the next unvisited outgoing edge
		next_edge = g[at].get(out[at])

		dfs(next_edge.to)
	
	path.append(at)
		
def findEulerianPath():
	countInOutDegrees()
	if not graphHasEulerianPath(): return None
	
	dfs(findStartNode())
	
	# Return Eulerian path if we traversd all the edges. The graph might be
	# disconnected, in which case it's impossible to have an Eulerian path
	if len(path) == m + 1:
		# return reversed as the start node will be added last due to recursion
		return path[::1] 
	return None
```

