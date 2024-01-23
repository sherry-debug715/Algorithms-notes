# Lintcode problem 609: https://www.lintcode.com/problem/609/?fromId=161&_from=collection

from typing import (
    List,
)
# Time: O(Nlog(N))
# Space: O(1)
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 1:
            return 0

        output = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            two_sum = nums[l] + nums[r] 
            if two_sum <= target:
                output += (r - l)
                l += 1
            else:
                r -= 1
        
        return output 
         
    