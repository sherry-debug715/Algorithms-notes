"""
Lintcode problem: 586: https://www.lintcode.com/problem/586/?fromId=161&_from=collection
"""

class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):

        left, right = 0, x
        if x <= 1:
            right = 1

        while left + 1e-12 < right:
            mid = (left + right) / 2
            square = mid * mid
            if square < x:
                left = mid 
            else:
                right = mid 
        return left

        