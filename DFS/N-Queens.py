# Lintcode problem 33: https://www.lintcode.com/problem/33

from typing import (
    List,
)

class Solution:
    """
    @param n: The number of queens
    @return: All distinct solutions
             we will sort your return value in output
    """
    def solve_n_queens(self, n: int) -> List[List[str]]:
        if not n:
            return "" 
        
        res = []
        self.search(res, n, [])
        return res 
    
    def search(self, res, n, cols):
        row = len(cols) 
        if len(cols) == n:
            res.append(self.draw_board(cols, n))
            return 
        
        for c in range(n):
            if self.is_valid(row, c, cols):
                cols.append(c) 
                self.search(res, n, cols)
                cols.pop() 
    
    def is_valid(self, r, c, cols):
        for row, col in enumerate(cols):
            if c == col:
                return False 
            if row - col == r - c or row + col == r + c:
                return False 
        
        return True 
    
    def draw_board(self, cols, n):
        board = []

        for c in cols:
            cur_col = "".join(["Q" if j == c else "." for j in range(n)])
            board.append(cur_col) 
        
        return board
