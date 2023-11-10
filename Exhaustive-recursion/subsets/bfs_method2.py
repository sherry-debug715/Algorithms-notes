from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]] 
        
        queue = [[]] 
        nums.sort()

        for n in nums:
            for i in range(len(queue)):
                subset = list(queue[i]) 
                subset.append(n) 
                queue.append(subset) 
        # for n in nums:
        #     queue += [subset + [n] for subset in queue]
        
        return queue
