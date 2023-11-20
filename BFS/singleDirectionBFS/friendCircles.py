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
    """
    initialize a variable, counter
    initialize a dictionary, visited
    iterate over neighbors:
        initialize a queue
        while queue:
            add all neighbors to the queue 
        counter += 1 
    return counter
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        counter = 0
        visited = {}

        for r in range(len(m)):
            visited[r] = False

        for n in range(len(m)):
            if visited[n]:
                continue

            queue = collections.deque([n])
            visited[n] = True
            counter += 1

            while queue:
                cur = queue.popleft()
                for c in range(len(m[cur])):
                    if not visited[c] and m[cur][c] == 1:
                        visited[c] = True
                        queue.append(c)
        
        return counter 
        