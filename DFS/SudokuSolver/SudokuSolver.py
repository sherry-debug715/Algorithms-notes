# Lintcode problem 802: https://www.lintcode.com/problem/802/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solve_sudoku(self, board: List[List[int]]):
        used = self.initial_build(board)
        self.dfs(board, used, 0)
        return board
    
    def dfs(self, board, used, index):
        if index == 81:
            return True 
        
        row, col = index // 9, index % 9 
        if board[row][col] != 0:
            return self.dfs(board, used, index + 1)

        for val in range(1, 10):
            if not self.valid(row, col, val, used):
                continue 
            
            board[row][col] = val
            used["row"][row].add(val)
            used["col"][col].add(val)
            used["box"][(row // 3 * 3) + (col // 3)].add(val)
            # the problem only require to look for one answer, therefore, stop code execution once one answer is found.
            if self.dfs(board, used, index + 1):
                return True 
            board[row][col] = 0
            used["row"][row].remove(val)
            used["col"][col].remove(val)
            used["box"][(row // 3 * 3) + (col // 3)].remove(val) 

        return False 
    
    def valid(self, row, col, val, used):
        if val in used["col"][col]:
            return False 
        
        if val in used["row"][row]:
            return False 
        
        if val in used["box"][(row // 3 * 3) + (col // 3)]:
            return False
        
        return True
    
    def initial_build(self, board):
        used = {
            "col": [set() for _ in range(9)],
            "row": [set() for _ in range(9)],
            "box": [set() for _ in range(9)]
        }

        n = len(board)
        for r in range(n):
            for c in range(n):
                if board[r][c] == 0:
                    continue 
                box_idx = (r // 3 * 3) + (c // 3)
                used["col"][c].add(board[r][c])
                used["row"][r].add(board[r][c])
                used["box"][box_idx].add(board[r][c])
        
        return used
