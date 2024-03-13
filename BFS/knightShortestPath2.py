# Lintcode problem 630: https://www.lintcode.com/problem/630/

from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        forward_direction = [
            (1, 2),
            (-1, 2),
            (2, 1),
            (-2, 1)
        ]

        backward_direction = [
            (-1, -2),
            (1, -2),
            (-2, -1),
            (2, -1) 
        ]

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1 

        n, m = len(grid), len(grid[0])
        forward_queue = deque([(0, 0)])
        forward_visited = set([(0, 0)])
        backward_queue = deque([(n - 1, m - 1)])
        backward_visited = set([(n - 1, m - 1)])
        distance = 0

        while forward_queue:
            distance += 1
            if self.find_joint(grid, forward_queue, forward_visited, backward_visited, forward_direction):
                return distance
        
        while backward_queue:
            distance += 1
            if self.find_joint(grid, backward_queue, backward_visited, forward_visited, backward_direction):
                return distance
        
        return -1 
    
    def find_joint(self, grid, queue, visited, other_visited, direction):
        def valid(row, col, grid):
            if row < 0 or row >= len(grid):
                return False 
            if col < 0 or col >= len(grid[0]):
                return False 
            if grid[row][col]:
                return False 
            if (row, col) in visited:
                return False 
            return True

        for _ in range(len(queue)):
            cur_r, cur_c = queue.popleft()
            for r, c in direction:
                next_r, next_c = cur_r + r, cur_c + c
                if (next_r, next_c) in other_visited:
                    return True 
                if valid(next_r, next_c, grid):
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c)) 
        return False


