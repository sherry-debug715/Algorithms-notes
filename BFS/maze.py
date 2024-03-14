# Lintcode problem 787: https://www.lintcode.com/problem/787/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if maze[destination[0]][destination[1]] == 1:
            return False 
        
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        queue = collections.deque([(start[0], start[1])]) 
        visited = set([(start[0], start[1])])

        while queue:
            row, col = queue.popleft()
            if row == destination[0] and col == destination[1]:
                return True 
            
            for r, c in directions:
                new_r, new_c = row + r, col + c 
                while 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]) and maze[new_r][new_c] != 1:
                    new_r += r 
                    new_c += c 
                new_r -= r 
                new_c -= c 
                if 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]) and (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
        return False 
