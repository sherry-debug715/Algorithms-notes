# Lintcode problem 398: https://www.lintcode.com/problem/398/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    """
    [
        (1, 0, 0), 
        (2, 0, 1), 
        (3, 1, 1), 
        (5, 1, 0)
    ]

    i = 3
    key = (1, 0)
    longest = {(0, 0): 1, (0, 1): 2, (1, 1): 3, (1, 0): 4}

    x = 1
    y = 1
    """
    # Time: O((row * col)log(row * col)): the most expensive step is sort function, as it sorts row * col points 
    #   from matrix
    # Space: O(N) where N is the total number of matrix[r][c]
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0 

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row_len = len(matrix)
        col_len = len(matrix[0])

        points = self.form_points(matrix, row_len, col_len) 
        length_tracker = {}

        for i in range(len(points)):
            cur_row, cur_col = points[i][1], points[i][2]
            key = (cur_row, cur_col)
            length_tracker[key] = 1 
            for (r, c) in directions:
                from_r = cur_row + r
                from_c = cur_col + c
                if from_r < 0 or from_r >= row_len or from_c < 0 or from_c >= col_len:
                    continue 
                if (from_r, from_c) in length_tracker and matrix[from_r][from_c] < points[i][0]:
                    length_tracker[key] = max(length_tracker[key], length_tracker[(from_r, from_c)] + 1) 
        
        return max(length_tracker.values())

    
    # form_points iterates over matrix, sort matrix by value while saving the coordinates of each value

    def form_points(self, matrix, row, col):
        points = [] 
        
        for r in range(row):
            for c in range(col):
                points.append((matrix[r][c], r, c)) 
        
        points.sort()
        return points
