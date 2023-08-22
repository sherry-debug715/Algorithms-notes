# Description
# Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
# Transformation rule such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary ))

# Example 1:
# start = "a"
# end = "c"
# dict =["a","b","c"]
# output = 2

# Example 2:
# start ="hit"
# end = "cog"
# dict =["hot","dot","dog","lot","log"]
# output = 5

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
        # if start and end are not in dict, add to dict 
        # adjacency list -> key should be all possible patterns of each word 
        # value should be a list of word from dict list that match the key after removing one letter 

        # use BFS to traverse through the adjacency list
        # use a set to remove dup 
        # the code should return LEVELS, instead of individual nodes.

        neighbors = self.find_neighbors(start, end, dict) 

        return self.count_ladder(start, end, neighbors)
    
    def find_neighbors(self, start, end, word_list): 
        neighbors = collections.defaultdict(list)

        if start not in word_list:
            word_list.add(start) 
        
        if end not in word_list:
            word_list.add(end)
        
        for word in word_list:
            for index in range(len(word)): 
                pattern = word[:index] + "*" + word[index + 1:] 
                neighbors[pattern].append(word) 
        
        return neighbors 
# {"h*t": [hit, hot], "*ot": [hot, dot, lot]}
    def count_ladder(self, start, end, adjacency_list):
        visited = set()
        queue = collections.deque([(start, 1)]) 

        while queue:
            cur, level = queue.popleft()

            if cur == end:
                return level

            for index in range(len(cur)): 
                pattern = cur[:index] + "*" + cur[index + 1:] 
                for word in adjacency_list[pattern]:
                    if word not in visited:
                        queue.append((word, level + 1))
                        visited.add(word) 
        
        return 0



