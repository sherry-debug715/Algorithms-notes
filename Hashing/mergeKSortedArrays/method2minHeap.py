from typing import (
    List,
)
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return [] 

        res = []
        # construct heap by adding the first element from each sub array to heap
        heap = [] 
        for idx, arr in enumerate(arrays):
            if arr:
                heapq.heappush(heap, (arr[0], idx, 0)) 
        
        while heap:
            min_val, arrIdx, val_idx = heapq.heappop(heap)
            res.append(min_val)
            next_idx = val_idx + 1
            if next_idx < len(arrays[arrIdx]):
                heapq.heappush(heap, (arrays[arrIdx][next_idx], arrIdx, next_idx)) 
        
        return res

        

