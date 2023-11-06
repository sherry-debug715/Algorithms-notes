from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        # create a new list of tuples, (number, index)
        # sort the new list 
        # use two pointers, left and right
        # while left < right 
            # num1, left_index = new_list[left]
            # num2, right_index = new_list[right]

            # if num1 + num2 > target:
                # decrement right
            # elif num1 + num2 < target:
                # increment left
            # else:
                # as we sorted the new list by value instead of index, therefore, 
                    # an extra step of checking the value of left_index and right_index is necessary. 

                # return [smaller_index, larger_index]

        new_numbers = [
            (num, index) for index, num in enumerate(numbers)
        ] # O(N)

        # new_sorted_numbers = sorted(new_numbers, key = lambda t: t[0])
        new_numbers.sort() # O(Nlog(N))

        left, right = 0, len(new_numbers) - 1

        while left < right:
            num1, left_index = new_numbers[left]
            num2, right_index = new_numbers[right]
            two_sum = num1 + num2 
            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                return sorted([left_index, right_index])


