"""
Lintcode problem 1179: https://www.lintcode.com/problem/1179/
"""

from typing import (
    List,
)

class Solution:
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        if not m:
            return 0 

        visited = set()
        output = 0
        n = len(m)

        def dfs(row):
            for neighbor in range(n):
                if neighbor in visited:
                    continue 

                if m[row][neighbor]:
                    visited.add(neighbor) 
                    dfs(neighbor)

        for student in range(n):
            if student in visited:
                continue 
            
            dfs(student)
            output += 1 
        
        return output 
    
        






