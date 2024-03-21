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
    # Time: O(Number of plans * N^2) where N^2 is the time to form a plan
    def solve_n_queens(self, n: int) -> List[List[str]]:
        if not n:
            return "" 
        
        res = []
        visited = {
            "col": set(),
            "sum": set(),
            "diff": set()
        }
        self.search(res, n, [], visited)
        return res 
    
    def search(self, res, n, cols, visited):
        if len(cols) == n:
            res.append(self.draw_board(cols, n))
            return 

        row = len(cols)
        for c in range(n):
            if self.is_valid(c, cols, visited):
                cols.append(c) 
                visited["col"].add(c)
                visited["sum"].add(row + c)
                visited["diff"].add(row - c)
                self.search(res, n, cols, visited)
                cols.pop() 
                visited["col"].remove(c)
                visited["sum"].remove(row + c)
                visited["diff"].remove(row - c)
    
    def is_valid(self, c, cols, visited):
        r = len(cols)
        if c in visited["col"]:
            return False 
        if r - c in visited["diff"] or r + c in visited["sum"]:
            return False 
        
        return True 
    
    def draw_board(self, cols, n):
        board = []

        for c in cols:
            cur_col = "".join(["Q" if j == c else "." for j in range(n)])
            board.append(cur_col) 
        
        return board
