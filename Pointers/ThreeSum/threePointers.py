from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        #.  |       
        # [-4, -1, -1, 0, 1, 2]
        #      |    
        #                    |

        # sort the given numbers list 
        # use 3 pointers 
        # for left in range(len(numbers) - 2)
            # mid, right = left + 1, len(numbers) - 1 
            # if left > 0 and numbers[left] == numbers[left-1]  
                # continue
            
            # while mid < right
                # if mid_val + right_val > -1 * left_val
                    # decrement right
                # elif < 
                    # increment mid
                # else
                    # add [left_val, mid_val, right_val] to output
                    # increment mid
                    # IMPORTANT, check if the next element next to mid is the same value. 

        # return output 

        if not numbers or len(numbers) < 3:
            return []

        numbers.sort()
        output = []

        for left in range(len(numbers) - 2):
            if numbers[left] > 0:
                break
            if left > 0 and numbers[left] == numbers[left - 1]:
                continue

            mid, right = left + 1, len(numbers) - 1
            target = 0 - numbers[left]
            while mid < right: 
                two_sum = numbers[mid] + numbers[right]
                if two_sum > target:
                    right -= 1 
                elif two_sum < target:
                    mid += 1 
                else:
                    output.append([numbers[left], numbers[mid], numbers[right]])
                    mid += 1
                    while numbers[mid] == numbers[mid - 1] and mid < right:
                        mid += 1

        return output
