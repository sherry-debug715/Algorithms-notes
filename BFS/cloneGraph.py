"""
Lintcode problem 137: https://www.lintcode.com/problem/137/?fromId=161&_from=collection
"""

from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""
""" 
edge case:
    if graph is empty:
        return None 
    all_nodes = get_nodes(node) #returns a set of all nodes of the graph.
    initialize a hash map, new_relationship.
    iterate over all_nodes:
        new_relationship[node] = new node  
    iterate over all nodes:
        for k in new_relationship:
            for n in k.neighbors:
                new_relationship[k].neighbors.append(new_relationship[n]) 
    
    return new_relationsip.node
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        root = node

        if not node:
            return None 
        
        all_nodes = self.get_nodes(node)
        new_relationship = {}
        
        for node in all_nodes:
            new_relationship[node] = UndirectedGraphNode(node.label) 
        
        for old_node in all_nodes:
            for n in old_node.neighbors:
                new_relationship[old_node].neighbors.append(new_relationship[n]) 
        
        return new_relationship[root]

    def get_nodes(self, node):
        visited = set([node]) 
        queue = collections.deque([node]) 

        while queue:
            cur = queue.popleft() 
            for n in cur.neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n) 

        return visited
