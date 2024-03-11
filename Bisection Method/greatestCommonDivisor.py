# Lintcode problem 845: https://www.lintcode.com/problem/845/

class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return -1 
        
        greater, smaller = a, b
        if a < b:
            greater, smaller = b, a 
        
        if greater % smaller == 0:
            return smaller 
        
        return self._gcd(greater, smaller)
    
    def _gcd(self, greater, smaller):
        if smaller != 0:
            return self._gcd(smaller, greater % smaller)

        return greater
