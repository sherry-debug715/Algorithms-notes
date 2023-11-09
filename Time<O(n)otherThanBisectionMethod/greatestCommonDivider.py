"""
lintcode problem 845: https://www.lintcode.com/problem/845/
"""
class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a: int, b: int) -> int:
        larger = a if a > b else b
        smaller = a if a < b else b 
        return self._gcd(larger, smaller)
    
    def _gcd(self, larger, smaller):
        if smaller != 0:
            return self._gcd(smaller, larger % smaller) 
        return larger
