"""
Lincode problem 517: https://www.lintcode.com/problem/517
"""

class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    """
    If num <= 0:
        return False 

    Initialize a list, prime_factors, [2, 3, 5]
    
    For each factor in prime_factors:
        While num is divisible by factor and not 1:
            Divide num by factor
        If num is 1, break 

    If num == 1:
        return True
    Else:
        return False
    """
    # Time: O(logN) the number of times n can be divided by each factors is logarithmic in relation to n
    # Space: O(1)
    def is_ugly(self, num: int) -> bool:
        if num <= 0:
            return False 
        
        prime_factors = [2, 3, 5] 

        for factor in prime_factors:
            while num % factor == 0 and num != 1:
                num = num / factor
            if num == 1: # pruning 
                break 
        
        if num == 1:
            return True 
        else:
            return False 
                
        

