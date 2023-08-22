## Use Cases

- Topological Sorting.
- Specific keywords or terms that are prominent or relevant within a particular connected component or subgraph.
- Traverse by level 
- Shortest path.

## Complexity 

- Time: O(n + m) n: nodes, m: vertices 
- Space: O(n)

## Pattern 
```py
 1. def bfs(start_node):

 2. # BFS must use queue structure intead of stack!

 3. # the distance dictionary can be used to track which nodes or vertices have been visited or processed. If a node has an entry in the distance dictionary, it means it has already been added to the queue, and thus shouldn't be added again, preventing cycles or redundant operations.

 4. # The other is to record the shortest distance from start_node to all other nodes.

 5. # If only connectivity is considered, just use a set.

 6. # When a node is used as a key, it is compared by its memory address.

 7. queue = collections.deque([start_node])

 8. distance = {start_node: 0}

 9. # While the queue is not empty, continuously take out a point from the queue and expand its neighbor nodes into the queue.

 11. while queue:

 12. node = queue.popleft()

 13. # If there is a clear destination/end point, you can add a judgment for the end point here.

 14. if node is the destination:

 15. break or return something

 16. for neighbor in node.get_neighbors():
 17. if neighor in distnace:

 18. continue

 19. queue.append(neighbor)

 20. distance[neighbor] = distance[node] + 1

 21.

 22. # If asked to return the distance from the starting point to all nodes, return hashmap

 23. return distance

 24. # If asked to return all connected nodes, then return all the nodes in the HashMap.

 25. return distance.keys()

 26. # If asked to return the distance to end node: 

 27. return distance[end_node]
```