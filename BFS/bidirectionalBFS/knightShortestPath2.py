"""
Lintcode problem 630
"""
from typing import (
    List,
)
"""

[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
"""

FORWARD_DIRECTIONS = [
    (1, 2),
    (- 1, 2),
    (2, 1),
    (- 2, 1),
]

BACKWARD_DIRECTIONS = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1)
]

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return -1 
        
        n, m = len(grid), len(grid[0])
        if grid[n - 1][m - 1]:
            return -1 
        if n * m == 1:
            return 0

        forward_queue = collections.deque([(0, 0)]) 
        backward_queue = collections.deque([(n - 1, m - 1)])
        forward_visited = set([(0, 0)]) 
        backward_visited = set([(n - 1, m - 1)]) 
        distance = 0

        while forward_queue and backward_queue:
            distance += 1 
            if self.find_joint(grid, forward_queue, forward_visited, FORWARD_DIRECTIONS, backward_visited):
                return distance 
            
            distance += 1
            if self.find_joint(grid, backward_queue, backward_visited, BACKWARD_DIRECTIONS, forward_visited):
                return distance 

        return -1 
    
    def find_joint(self, grid, queue, visited, DIRECTIONS, other_visited):
        for _ in range(len(queue)):
            cur_r, cur_c = queue.popleft() 
            for (r, c) in DIRECTIONS:
                next_r, next_c = cur_r + r, cur_c + c
                if self.inbound(next_r, next_c, grid, visited):
                    if (next_r, next_c) in other_visited:
                        return True 
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c)) 

        return False
    
    def inbound(self, r, c, grid, visited):
        if (r, c) in visited:
            return False
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0



