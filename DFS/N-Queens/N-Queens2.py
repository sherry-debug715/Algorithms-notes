# Lintcode problem 34: https://www.lintcode.com/problem/34/description

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    # Time: O(N!)
    def total_n_queens(self, n: int) -> int:
        if not n:
            return 0 
        
        visited = {
            "col": set(),
            "sum": set(),
            "diff": set()
        }
        res = [0]
        self.search(n, visited, [], res)
        return res[0] 
    
    def search(self, n, visited, cols, res):
        if len(cols) == n:
            res[0] += 1
            return 
        
        row = len(cols)
        for col in range(n):
            if not self.valid(row, col, visited):
                continue 
            
            cols.append(col)
            visited["col"].add(col)
            visited["sum"].add(row + col)
            visited["diff"].add(row -  col)
            self.search(n, visited, cols, res)
            cols.pop()
            visited["col"].remove(col)
            visited["sum"].remove(row + col)
            visited["diff"].remove(row - col)
    
    def valid(self, r, c, visited):
        if c in visited["col"]:
            return False 
        
        if r + c in visited["sum"] or r - c in visited["diff"]:
            return False 
        
        return True 
