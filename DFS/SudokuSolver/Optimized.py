from typing import (
    List,
)

class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solve_sudoku(self, board: List[List[int]]):
        if self.dfs(board):
            return board
    
    def dfs(self, board):
        #  example: i, j, choices =  3 5 [6]
        # every time, get_least_choices_grid comes back with numbers/number that could possibly be placed at board[i][j]
        i, j, choices = self.get_least_choices_grid(board)
        if i is None:
            return True 
        
        for num in choices:
            board[i][j] = num 
            if self.dfs(board):
                return True 
            board[i][j] = 0
    
    def get_least_choices_grid(self, board):
        x, y, choices = None, None, [0] * 10 

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue 
                vals = []
                for val in range(1, 10):
                    if self.is_valid(board, i, j, val):
                        vals.append(val) 
                if len(vals) < len(choices):
                    x, y, choices = i, j, vals 
        
        return x, y, choices 
    
    def is_valid(self, board, r, c, val):
        for i in range(9):
            if board[r][i] == val:
                return False 
            if board[i][c] == val:
                return False 
            if board[r // 3 * 3 + i // 3][c // 3 * 3 + i % 3] == val:
                return False 
        
        return True 
