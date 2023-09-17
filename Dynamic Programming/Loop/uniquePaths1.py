"""
Lintcode problem 114: https://www.lintcode.com/problem/114/
""" 

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    """
    [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    m is row
    n is col

    Top down method 
    Initialize a 2d list, grid, with n and m, each inner list should be filled with 0 
    Fill the first row and first column with 1 
    For range 1, m, with r:
        for range 1, n, with c:
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1] 

    return grid[m - 1][n - 1] 
    
    """
    def unique_paths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)] 
        for c in range(n):
            grid[0][c] = 1 
        
        for r in range(m):
            grid[r][0] = 1 

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[m - 1][n -1]
