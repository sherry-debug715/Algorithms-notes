"""
Lintcode problem 140: https://www.lintcode.com/problem/140/
"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    a^n = (a^2/n)^2 = a^2 % b 
    """
    # Time: O(log(n))
    # Space: O(log(n)) 
    def fast_power(self, a: int, b: int, n: int) -> int:
        if a == 0:
            return 0 
        if n == 1:
            return a % b 
        if n == 0:
            return 1 % b
        
        power = self.fast_power(a, b, n // 2) 
        power = (power * power) % b
        # if n is an odd number. 
        if n % 2 != 0:
            power = (power * a) % b 
        
        return power 

