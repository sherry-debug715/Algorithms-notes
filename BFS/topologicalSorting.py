"""
Lintcode problem 127: https://www.lintcode.com/problem/127/?fromId=161&_from=collection
"""

"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def form_levels(self, graph):
        levels = {node: 0 for node in graph}
        for node in graph:
            for n in node.neighbors:
                levels[n] = levels.get(n, 0) + 1 
        return levels 

    def topSort(self, graph):
        levels = self.form_levels(graph)
        queue = collections.deque([node for node in levels if levels[node] == 0])
        top = []
        while queue:
            cur = queue.popleft()
            top.append(cur)
            
            for node in cur.neighbors:
                levels[node] -= 1
                if levels[node] == 0:
                    queue.append(node)
        
        return top 
