from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    # Time: O(n)
    # Space: O(1)
    def can_jump(self, a: List[int]) -> bool:
        if not a:
            return False 
        
        gas = 0
        for n in a:
            if gas < 0:
                return False 
            elif n > gas:
                gas = n
            gas -= 1 
        
        return True