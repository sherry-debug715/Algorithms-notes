# lintcode problem 59: https://www.lintcode.com/problem/59/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    # Time: O(N^2)
    # Space: O(1)
    def three_sum_closest(self, numbers: List[int], target: int) -> int:
        if not numbers:
            return 0 

        numbers.sort()
        _sum = numbers[0] + numbers[1] + numbers[-1] 

        for l in range(len(numbers) - 2):
            mid, right = l + 1, len(numbers) - 1
            if l > 0 and numbers[l] == numbers[l - 1]:
                continue 
            while mid < right:
                cur_sum = numbers[l] + numbers[mid] + numbers[right]
                if abs(cur_sum - target) < abs(_sum - target):
                    _sum = cur_sum 
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    mid += 1  
                else:
                    return target 
        
        return _sum
            


