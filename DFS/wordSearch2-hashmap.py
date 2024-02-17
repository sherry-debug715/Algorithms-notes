# Lintcode problem 132: https://www.lintcode.com/problem/132/

from typing import (
    List,
)

ROWDI = [-1, 1, 0, 0]
COLDI = [0, 0, -1, 1]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    """
    ROWDI = [-1, 1, 0, 0]
    COLDI = [0, 0, -1, 1]
    initialize a empty list, res.
    build a matrix based on board input, visited
    build a prefix dictionary based on words input. helper function get_prefix
    iterate over the board by row and col:
        if board[row][col] in prefix_dic and visited[row][col] not true:
            mark the as visited
            call dfs function with, row, col, visited, prefix_dic, res, board[row][col], board
            back track row and col as unvisited 
    return res 

    fn dfs(r, c, visited, prefix_dic, res, cur_word):
        if prefix_dic[cur_word]:
            add cur_word to res 
        
        if cur_word not in prefix_dic:
            return 
        
        for idx in range(4):
            new_r = r + ROWDI[idx]
            new_c = c + COLDI[idx]
            if fn inbound(new_r, new_c, visited):
                add it to visited
                self.dfs(new_r, new_c, visited, prefix_dic, res, cur_word + board[new_r][new_c], board)
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        visited = [[False] * len(board[0]) for _ in range(len(board))] 
        prefix_dic = self.get_prefix(words)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in prefix_dic and not visited[row][col]:
                    visited[row][col] = True
                    self.dfs(row, col, visited, prefix_dic, res, board[row][col], board)
                    visited[row][col] = False 
        
        return list(res)
    
    def dfs(self, row, col, visited, prefix_dic, res, cur_word, board):
        if cur_word not in prefix_dic:
            return 

        if prefix_dic[cur_word]:
            res.add(cur_word)
        
        for idx in range(4):
            new_r = row + ROWDI[idx]
            new_c = col + COLDI[idx]
            # print("in here", new_r)
            if self.inbound(new_r, new_c, visited, board):
                visited[new_r][new_c] = True
                # print("cur_word + board[new_r][new_c]", cur_word + board[new_r][new_c])
                self.dfs(new_r, new_c, visited, prefix_dic, res, cur_word + board[new_r][new_c], board) 
                visited[new_r][new_c] = False
    
    def inbound(self, row, col, visited, board):
        if row < 0 or row >= len(board):
            return False 
        
        if col < 0 or col >= len(board[0]):
            return False

        if visited[row][col]:
            return False
        
        return True
        
    
    def get_prefix(self, words):
        prefix_dic = {}
        for word in words:
            for idx in range(len(word)):
                prefix = word[:idx + 1]
                if prefix not in prefix_dic:
                    prefix_dic[prefix] = False 
                # it's important not to check if word is already in prefix_dic
                # especially for the following situation:
                # "abcd", "abc"
                prefix_dic[word] = True 
        
        return prefix_dic