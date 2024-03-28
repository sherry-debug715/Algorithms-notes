# Lintcode problem 894: https://www.lintcode.com/problem/894/description

from typing import (
    List,
)
# Time: O(N^2)
# Space: O(1)
class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancake_sort(self, array: List[int]):
        if not array:
            return 
        
        for i in range(len(array) - 1, -1, -1):
            max_idx = self.find_max_index(array, i)
            if max_idx is None:
                continue
            FlipTool.flip(array, max_idx)
            FlipTool.flip(array, i)

        return array
    
    # given an index, the function should return the index of the max value from
    # subarr arr[:idx] 
    def find_max_index(self, arr, index):
        max_idx = None
        max_val = arr[index] 

        for idx, val in enumerate(arr):
            if idx == index:
                break
            if val > max_val:
                max_val = val 
                max_idx = idx 

        return max_idx


