"""
Leetcode 785: https://leetcode.com/problems/is-graph-bipartite/description/
"""

"""
Initialize 2 instance variables, green, and red. 
Initialize an list populated with None, at length of graph, visited
Iterate over graph, with index nodeList:
    if visited[nodeList] is None:
        valid = dfs(nodeList, self.green, graph, visited):
        if not valid:
            return False 
return True

def function(idx, color, graph, visited)
    visited[idx] = self.green
    neighbor = oppsite color of color.
    iterate over graph[idx], with n:
        if visited[n] is None:
            dfs(n), neighbor, graph, visited)
        elif visited[n] != neighbor:
            return False 
    return True
"""
class Solution:
    def __init__(self):
        self.green = "green"
        self.red = "red"

    def isBipartite(self, graph: List[List[int]]) -> bool:       
        visited = [None] * len(graph)

        for node in range(len(graph)):
            if visited[node] is None:
                if not self.dfs(node, self.green, graph, visited):
                    return False 
        return True
    
    def dfs(self, idx, color, graph, visited):
        visited[idx] = color 
        neighbor = self.red if color == self.green else self.green 

        for n in graph[idx]:
            if visited[n] is None:
                if not self.dfs(n, neighbor, graph, visited):
                    return False
            elif visited[n] != neighbor:
                return False 
        return True

# Method 2: highly inefficient
    from typing import (
    List,
)

class Node:
    def __init__(self, val):
        self.val = val
        self.color = None
        self.neighbors = []

class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """

    def is_bipartite(self, graph: List[List[int]]) -> bool:
        def form_graph():
            neighbors = {num: Node(num) for num in range(len(graph))}
            
            for r in range(len(graph)):
                for n in graph[r]:
                    cur_node = neighbors[r]
                    neighbor = neighbors[n]
                    if neighbor not in cur_node.neighbors:
                        cur_node.neighbors.append(neighbor)
                        neighbor.neighbors.append(cur_node)
            return neighbors
        
        neighbors = form_graph() 

        def dfs(node, color):
            if node.color:
                return node.color == color

            node.color = color

            return all(dfs(neighbor, 1 - color) for neighbor in node.neighbors)

        for each_node in neighbors.values():
            if each_node.color is None and not dfs(each_node, 0):
                return False 
        return True

        
    
