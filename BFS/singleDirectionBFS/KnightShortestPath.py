"""
lintcode problem 611: https://www.lintcode.com/problem/611/
"""

from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        rs, rc = source.x, source.y
        queue = collections.deque([(rs, rc, 0)])
        visited = set((rs, rc)) 

        while queue:
            (r, c, level) = queue.popleft()
            if r == destination.x and c == destination.y:
                return level 
            neighbors = self.find_neighbors(grid, r, c)
            for (row, col) in neighbors:
                if (row, col) not in visited:
                    visited.add((row, col))
                    queue.append((row, col, level + 1))

        return -1

    def find_neighbors(self, grid, x, y):
        pos = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1),
        ]

        return [(r, c) for (r, c) in pos if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 1]
