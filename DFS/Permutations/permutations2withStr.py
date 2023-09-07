"""
Description
Given a string, find all permutations of it without duplicates.

s = "aabb"
output = ["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""

from typing import (
    List,
)

class Solution:
    """
    @param str: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        if not s:
            return [""] 
        char = sorted(list(s))
        res = [] 
        visited = [False] * len(char)
        self.dfs(char, visited, res, [])
        return res 
    
    def dfs(self, char, visited, res, permutate):

        if len(permutate) == len(char):
            res.append("".join(permutate))
            return 

        for i in range(len(char)):
            if visited[i]:
                continue 
            # making sure visited[i - 1] is False is very important step of avoiding duplicates.
            # res = ["abb", "bab", "bba"]
            # visited = [False, False, False]
            #                    i
            # char = ["a", "b", "b"]
            # if char[i] == char[i - 1] but char[i - 1] is not visited, continuing code execution will create another permutate duplicate of [b, a, b]
            if i > 0 and char[i] == char[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True 
            permutate.append(char[i])
            self.dfs(char, visited, res, permutate)
            permutate.pop()
            visited[i] = False

