from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        left = 0 
        output = []
        initial = sum(nums[:k])
        output.append(initial) 

        for right in range(k, len(nums)):
            cur_sum = initial + nums[right] - nums[left]
            output.append(cur_sum)
            initial = cur_sum 
            left += 1
        
        return output 

