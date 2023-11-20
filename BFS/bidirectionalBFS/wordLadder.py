"""
Leetcode problem 127: https://leetcode.com/problems/word-ladder/description/
"""

from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord) 
        
        graph = self.form_graph(wordList) 
        
        return self.bfs(graph, beginWord, endWord) 
    
    def form_graph(self, wordList):
        graph = defaultdict(list) 

        for word in wordList:
            for i in range(len(word)):
                prefix = word[:i]
                pattern = prefix + "*" + word[i + 1:] 
                graph[pattern].append(word) 
        
        return graph 
    
    def bfs(self, graph, beginWord, endWord): 
        start_queue = deque([beginWord])
        end_queue = deque([endWord]) 
        start_visited = set([beginWord])
        end_visited = set([endWord]) 
        distance = 0

        while start_queue and end_queue:
            distance += 1 
            if self.find_joint(graph, start_queue, start_visited, end_visited):
                return distance 
            
            distance += 1
            if self.find_joint(graph, end_queue, end_visited, start_visited):
                return distance 
        
        return 0 
    
    def find_joint(self, graph, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            cur = queue.popleft() 
            if cur in opposite_visited:
                return True 
            for i in range(len(cur)):
                prefix = cur[:i]
                pattern = prefix + "*" + cur[i + 1:] 
                for n in graph[pattern]:
                    if n in visited:
                        continue 
                    visited.add(n)
                    queue.append(n) 
                    
        return False 


        