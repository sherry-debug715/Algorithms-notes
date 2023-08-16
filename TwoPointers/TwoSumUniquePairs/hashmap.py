from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    # Time: O(N)
    # Space: O(N)
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        pair = 0
        hashmap = {}

        if not nums or len(nums) == 1:
            return pair
        
        for num in nums:
            diff = target - num  
            if diff in hashmap and hashmap[diff] is None:
                hashmap[diff] = 1
                pair += 1 
                hashmap[num] = 1
            if num not in hashmap:
                hashmap[num] = None 
                
        return pair 