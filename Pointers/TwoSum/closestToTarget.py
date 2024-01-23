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
        n = len(nums)

        nums.sort() 
        # check if nums array only contain one unique number
        if nums[0] == nums[-1]:
            return abs(target - nums[0])

        l, r = 0, n - 1 
        min_diff = float("inf") 

        while l < r:
            two_sum = nums[l] + nums[r] 
            # pruning 
            if two_sum == target:
                return 0
            if abs(target - two_sum) < min_diff:
                min_diff = abs(target - two_sum)
            if two_sum < target:
                l += 1
                # handling duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            else:
                r -= 1 
                # handling duplicates
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
        
        return min_diff