# Lintcode problem 235: https://www.lintcode.com/problem/235/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def prime_factorization(self, num: int) -> List[int]:
        if num == 0:
            return []
        if num == 1:
            return [1]
        
        output = []
        i = 2
        while i * i <= num:
            while num % i == 0:
                output.append(i)
                num = num // i 
            i += 1
        
        if num > 1:
            output.append(num)
        
        return output 
