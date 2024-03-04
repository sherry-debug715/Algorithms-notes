# Lintcode problem 845: https://www.lintcode.com/problem/845/?fromId=161&_from=collection
# 欧几里得算法： gcd(a, b) = gcd(b, a mod b), given a > b and a > 0 and b > 0.
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
