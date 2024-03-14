# Lintcode problem 121: https://www.lintcode.com/problem/121/

from typing import (
    List,
    Set,
)
from collections import deque, defaultdict

class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def form_graph(self, word_list):
        graph = defaultdict(list) 

        for word in word_list:
            for i in range(len(word)):
                prefix = word[:i]
                pattern = prefix + "*" + word[i + 1:] 
                graph[pattern].append(word) 
        
        return graph 

    def find_ladders(self, start: str, end: str, dict: Set[str]) -> List[List[str]]:
        if start == end:
            return [[start]] 

        dict.add(start)
        dict.add(end)
        graph = self.form_graph(dict)

        output = []
        visited = set([start])
        queue = deque([(start, [start])])

        while queue:
            cur_word, cur_path = queue.popleft()
            if cur_word == end:
                output.append(cur_path)
                continue 

            for i in range(len(cur_word)):
                pattern = cur_word[:i] + "*" + cur_word[i + 1:]
                for word in graph[pattern]:
                    if word in visited:
                        continue 
                    visited.add(word)
                    queue.append((word, [*cur_path, word])) 

        return output  