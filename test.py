from typing import (
    Set,
)

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
        
        if start not in dict:
            dict.add(start) 
        if end not in dict:
            dict.add(end) 
        
        neighbors = self.form_graph(dict) 
        print("neighbors", neighbors)
        return neighbors
    
    def form_graph(self, dict):
        neighbors = {} 

        for letter in dict:
            for i in range(len(letter)):
                prefix = letter[:i]
                pattern = prefix + "*" + letter[i + 1:]
                neighbors[pattern] = [] 
        
        for letter in dict:
            for i in range(len(letter)):
                prefix = letter[:i]
                pattern = prefix + "*" + letter[i + 1:]
                if pattern in neighbors:
                    neighbors[pattern].append(letter)

        return neighbors

test = Solution()
print(test.ladder_length("hit", "cog", {"hot","dot","dog","lot","log"}))