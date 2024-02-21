# Lintcode problem 544: https://www.lintcode.com/problem/544/description?fromId=161&_from=collection

from typing import (
    List,
)
import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    # Time: O(NlogN) where N is the length of nums, logN time for heappop from root
    # Space: O(N)
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        largest = [None] * k 
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            cur = heapq.heappop(nums) 

        cur_idx = len(largest) - 1
        for _ in range(k):
            largest[cur_idx] = heapq.heappop(nums) 
            cur_idx -= 1
        
        return largest



