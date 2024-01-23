# Lintcode problem 533: https://www.lintcode.com/problem/533/?fromId=161&_from=collection

from typing import (
    List,
)
# Time: O(NlogN)
# Space: O(1)
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def two_sum_closest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 
        
        nums.sort() # O(NlogN) 
        l, r = 0, len(nums) - 1 
        min_diff = float("inf") 

        while l < r: # O(N)
            two_sum = nums[l] + nums[r] 
            if abs(target - two_sum) < min_diff:
                min_diff = abs(target - two_sum)
            if two_sum < target:
                l += 1
            else:
                r -= 1 
        
        return min_diff