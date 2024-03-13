# Lintcode problem 761: https://www.lintcode.com/problem/761/

from typing import (
    List,
)

class Solution:
    """
    @param arr: an array of non-negative integers
    @return: minimum number of elements
    """
    def min_elements(self, arr: List[int]) -> int:
        queue = [[]]
        total = sum(arr) 
        for n in arr:
            for i in range(len(queue)):
                subset = list(queue[i]) 
                cur_sum = sum(subset)
                diff = total - cur_sum 
                if cur_sum > diff:
                    return len(subset) 
                subset.append(n)
                queue.append(subset) 
        return -1 


