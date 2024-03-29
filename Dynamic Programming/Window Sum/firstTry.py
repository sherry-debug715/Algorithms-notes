# Lintcode problem 604: https://www.lintcode.com/problem/604/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    output = [10, 17, 20, 15 ]
    sum = 
         i
    [1,2,7,8,5]
               j
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [] 
        
        j, window_sum = 0, 0
        output = []

        for i in range(len(nums) - k + 1):
            while j < len(nums) and j - i < k:
                window_sum += nums[j] 
                j += 1 

            output.append(window_sum)
            window_sum -= nums[i] 
        
        return output 

