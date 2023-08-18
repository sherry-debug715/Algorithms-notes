from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        start, end = 0, len(nums) - 1 
        # to avoid start == end situation which will lead to infinite looping.
        while start + 1 < end: 
            mid = start + (end - start) // 2 
            if nums[mid] < target: 
                start = mid + 1 
            elif nums[mid] > target:
                end = mid - 1
            else:
                end = mid 
#             L
#[1,4,4,5,7,7,8,9,9,10] 9
#               M
#               E    

        if start < len(nums) and nums[start] == target:
            return start 
        if end < len(nums) and nums[end] == target:
            return end 
        return -1
#      M
#  S
# [1,4,4,5,7,7,8,9,9,10]. 4
#          E