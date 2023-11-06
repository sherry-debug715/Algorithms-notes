from typing import (
    List,
)
# Time O(n)
# Space O(n)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        # use a list to hold result
        # use a hashmap to store difference as key and index as value 
        # iterate over the numbers list 
            # check if current value is in the hashmap
                # true -> push the value of hashmap[value] to result list 
                #   and push current index to result list.   
            # add difference to hashmap 
        
        res = []
        difference = {}

        for (index, val) in enumerate(numbers):
            diff = target - val 
            if val in difference:
                res.append(difference[val])
                res.append(index)

            difference[diff] = index 

        return res 