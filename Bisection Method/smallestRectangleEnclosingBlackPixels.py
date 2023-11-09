"""
Lintcode problem 600: https://www.lintcode.com/problem/600/
"""

from typing import (
    List,
)

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    """
    [
        "0100"
        "1110",
        "1100",
        "0100",
        "0000"
    ]
    """
    """
    if image is empty:
        return 0 
    initialize two variables, n, m, set them to length of image and length of image[0].
    up: check from row 0 to x, find the first row with "1" using binary search in O(nlogn) time
    down: check from row x to n - 1, find the last row with "1"
    left: check from col 0 to y, find the left-most col with "1"
    right: check from col y to m - 1, find the right-most col with "1"

    return (right - left + 1) * (down - up + 1) 
    """
    # Time: O(nlogn) -> O(nlogm + mlogn)
    # Space: O(1)
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        if not image:
            return 0 

        n, m = len(image), len(image[0]) 

        up = self.find_first(image, 0, x, self.check_row) 
        down = self.find_last(image, x, n - 1, self.check_row)
        left = self.find_first(image, 0, y, self.check_col)
        right = self.find_last(image, y, m - 1, self.check_col) 

        return (right - left + 1) * (down - up + 1) 
    
    def find_first(self, image, start, end, func):
        while start + 1 < end:
            mid = (start + end) // 2 
            if func(image, mid):
                end = mid 
            else:
                start = mid 

        if func(image, start):
            return start 
        return end

    def find_last(self, image, start, end, func):
        while start + 1 < end:
            mid = (start + end) // 2 
            if func(image, mid):
                start = mid 
            else:
                end = mid 
        
        if func(image, end):
            return end
        return start 

    def check_row(self, image, row):
        for c in range(len(image[0])):
            if image[row][c] == "1":
                return True 
        return False 

    def check_col(self, image, col):
        for r in range(len(image)):
            if image[r][col] == "1":
                return True 
        return False 



