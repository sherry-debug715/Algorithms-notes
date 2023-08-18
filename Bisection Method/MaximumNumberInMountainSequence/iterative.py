from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        # find the number it's right and left side numbers are both less than its value 
        # increment: left < n < right 
        # decrement: left > n > right 
        # looking for: left < n > right 
        #  L 
        # [10, 9, 8, 7]
        #      R
        #.     M
        # if left_val > right_val return left_val else return right_val 

        #. L
        # [1, 2, 4, 8, 6, 3] 
        #.                R
        #           M

        if not nums:
            return -1 
        
        start, end = 0, len(nums) -  1 

        while start + 1 < end: 
            mid = (start + end) // 2 

            if nums[mid - 1] < nums[mid] < nums[mid + 1]: 
                start = mid
                continue 
            if nums[mid - 1] > nums[mid] > nums[mid + 1]:
                end = mid 
                continue 
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return nums[mid]
        
        if nums[start] > nums[end]:
            return nums[start] 
        else:
            return nums[end]
            
            
            

