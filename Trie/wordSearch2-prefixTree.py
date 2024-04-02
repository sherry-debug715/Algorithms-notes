# Lintcode problem 132: https://www.lintcode.com/problem/132/

from typing import (
    List,
)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 
        self.refs = 0
    
    def insert(self, word):
        cur = self 
        cur.refs = 1
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
            cur.refs += 1
        cur.endOfWord = True 
    
    def removeWord(self, word):
        cur = self
        cur.refs -= 1 
        for l in word:
            if l in cur.children:
                cur = cur.children[l] 
                cur.refs -= 1

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build prefix tree
        root = TrieNode() 
        visited, res = set(), set()

        for word in words:
            root.insert(word) 

        def dfs(row, col, cur_word, node):
            if row < 0 or row == len(board):
                return 
            if col < 0 or col == len(board[0]):
                return 
            if (row, col) in visited:
                return 
            if board[row][col] not in node.children:
                return 
            if node.children[board[row][col]].refs < 1:
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            cur_word += board[row][col]
            if node.endOfWord:
                node.endOfWord = False
                res.add(cur_word)
                root.removeWord(cur_word)

            dfs(row - 1, col, cur_word, node)
            dfs(row + 1, col, cur_word, node)
            dfs(row, col - 1, cur_word, node)
            dfs(row, col + 1, cur_word, node)
            visited.remove((row, col))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, "", root) 

        return list(res)

        
