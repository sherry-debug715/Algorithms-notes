from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    """
        edge case:
            if nums list is empty:
                return [-1, -1]

        initialize a variable, j, set it to -1.
        from range 0 to the last second element of nums, with i:
            j = the return of a helper function, binary_search         
            if j != -1:
                return [nums[i], nums[j]]

        return [-1, -1]
    """
    """
    binary_search(i + 1, len(nums) - 1, target + nums[i]):
        standard process 
        return -1 if no match
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1] 

        j = -1 
        for i in range(len(nums) - 1):
            j = self.binary_search(i + 1, len(nums) - 1, target + nums[i], nums) 
            if j != -1:
                return [nums[i], nums[j]]

        return [-1, -1] 

    def binary_search(self, start, end, diff, nums):
        while start + 1 < end:           
            mid = (start + end) // 2 
            if nums[mid] < diff:
                start = mid 
            else:
                end = mid 

        if nums[start] == diff:
            return start 
        elif nums[end] == diff:
            return end 

        return -1  