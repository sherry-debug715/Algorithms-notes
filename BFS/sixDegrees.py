# Lintcode problem 531: https://www.lintcode.com/problem/531/?fromId=161&_from=collection

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        if s.label == t.label:
            return 0

        forward_queue = deque([s])
        forward_visited = set([s.label])
        backward_queue = deque([t])
        backward_visited = set([t.label])
        distance = 0

        while forward_queue and backward_queue:
            distance += 1
            if self.find_joint(forward_queue, forward_visited, backward_visited):
                return distance
            
            distance += 1
            if self.find_joint(backward_queue, backward_visited, forward_visited):
                return distance
        return -1
    
    def find_joint(self, queue, visited, other_visited):
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            for n in cur_node.neighbors:
                if n.label in other_visited:
                    return True
                if n.label not in visited:
                    visited.add(n.label)
                    queue.append(n)
        return False 
