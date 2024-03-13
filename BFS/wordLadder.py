# Lintcode problem 120: https://www.lintcode.com/problem/120/

from typing import (
    Set,
)

from collections import deque
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        if len(start) == 0 or len(end) == 0:
            return 0 
        if start == end:
            return 1
        
        if start not in dict:
            dict.add(start) 
        if end not in dict:
            dict.add(end) 
        
        neighbors = self.form_graph(dict) 

        return self.bfs(start, end, neighbors)
    
    def form_graph(self, dict):
        neighbors = collections.defaultdict(list)
        
        for letter in dict:
            for i in range(len(letter)):
                prefix = letter[:i]
                pattern = prefix + "*" + letter[i + 1:]
                neighbors[pattern].append(letter)

        return neighbors
    
    def bfs(self, start, end, neighbors):
        start_queue, end_queue = deque([start]), deque([end]) 
        start_visited, end_visited = set([start]), set([end]) 
        distance = 0

        while start_queue and end_queue:
            distance += 1 
            if self.find_joint(start_queue, neighbors, start_visited, end_visited):
                return distance 
            
            distance += 1 
            if self.find_joint(end_queue, neighbors, end_visited, start_visited):
                return distance

        return 0
    
    def find_joint(self, queue, graph, visited, opposite_visited):
        for _ in range(len(queue)):
            cur = queue.popleft() 
            if cur in opposite_visited:
                return True

            for i in range(len(cur)):
                prefix = cur[:i]
                pattern = prefix + "*" + cur[i + 1:]

                for n in graph[pattern]:
                    if n in visited:
                        continue 
                    queue.append(n)
                    visited.add(n) 
        return False

