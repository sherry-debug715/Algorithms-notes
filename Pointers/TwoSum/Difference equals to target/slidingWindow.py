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
    -2
               i 
    [0,5,7]
                        j
    """
    # Time: O(N)
    # Space: O(1)
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return 
            
        target = abs(target)
        n = len(nums)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                if nums[j] - nums[i] < target:
                    j += 1
                elif nums[j] - nums[i] > target:
                    i += 1
                    if i == j:
                        break 
                else:
                    return [nums[i], nums[j]]


