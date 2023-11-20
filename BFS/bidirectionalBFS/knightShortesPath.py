from typing import (
    List,
)
from lintcode import (
    Point,
)
from collections import deque


"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

DIRECTION = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, - 2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    """
    Initialize a list, DIRECTION, it should holds all directions that the knight can take in one step.
    Edge case:
        if grid is empty:
            return -1 
        if start is the end:
            return 0
        if start is a block:
            return -1

    Initalize a number, distance, set it to 0
    Initialize two queues, forward and backward, populate both queues with source and destination points respectively. 
    Initialize two sets, forward_visited and backward_visited, populate them with source and destination points respectively. 

    while forward and backward are not empty:
        distance += 1
        Iterate over the current level in forward queue, helper function, returns boolean.
        if helper function is True:
            return distance
        
        distance += 1
        Iterate over the current level in forward queue, helper function, returns boolean.
        if helper function is True:
            return distance
              
    return -1 
    """
    # Time (O(sqrN))
    # Space(O(N))
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        if not grid or not grid[0]:
            return -1 
        if source.x == destination.x and source.y == destination.y:
            return 0
        if grid[source.x][source.y] == 1:
            return -1
        
        distance = 0
        forward, backward = deque([(source.x, source.y)]), deque([(destination.x, destination.y)]) 
        forward_visited, backward_visited = set([(source.x, source.y)]), set([(destination.x, destination.y)])

        while forward and backward:
            distance += 1 
            if self.find_joint(grid, forward, forward_visited, backward_visited):
                return distance 

            distance += 1 
            if self.find_joint(grid, backward, backward_visited, forward_visited):
                return distance 

        return -1
    
    def find_joint(self, grid, queue, visited, other_visited):
        for _ in range(len(queue)):
            row, col = queue.popleft() 
            for (r, c) in DIRECTION:
                new_row, new_col = row + r, col + c
                if (new_row, new_col) in other_visited:
                    return True 
                if self.inbound(new_row, new_col, grid, visited):
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
        
        return False
    
    def inbound(self, row, col, grid, visited):
        if (row, col) in visited:
            return False 
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 1










