# Lintcode problem 608: https://www.lintcode.com/problem/608/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    # Time: O(N)
    # Space: O(1)
    # No need to check if nums is empty or have length of 1 since the instruction stated that each input would have exactly one solution
    def two_sum(self, nums: List[int], target: int) -> List[int]:        
        l, r = 0, len(nums) - 1 

        while l < r:
            two_sum = nums[l] + nums[r] 
            if two_sum == target:
                return [l + 1, r + 1] 
            if two_sum < target:
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            else:
                r -= 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1 
        
        return None 
