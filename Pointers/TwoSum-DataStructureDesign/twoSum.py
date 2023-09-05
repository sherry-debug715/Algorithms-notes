"""
Description
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
"""

class TwoSum:
    def __init__(self):
        self.nums = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.nums.append(number)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # if nums is empty of it only has one element, return False 
        # use hashset to store difference.
        # iterate over nums, add value to hashset, check if difference is in 
        # hashset, if true, return True 

        if not self.nums or len(self.nums) == 1:
            return False 
        
        hashset = set()

        for n in self.nums:
            diff = value - n 
            if diff in hashset:
                return True 
            hashset.add(n) 

        return False