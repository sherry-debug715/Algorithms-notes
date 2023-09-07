"""
Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

LintCode Problem 425, Link: https://www.lintcode.com/problem/425/?fromId=161&_from=collectiona
"""
from typing import (
    List,
)

class Solution:
    """
    @param digits: A digital string
    @return: all possible letter combinations
             we will sort your return value in output
    """
    """
    1. Initialize a hash map, num_letters, its keys are numbers and values are strings of respected letters
    2. Initialize a list, res, to store final results
    3. use a helper function dfs, which takes in the following argument: digits, num_letters, res, start_index, cur_comb which is a list
        1. if length of cur_comb == length of digits: convert cur_comb into a string then add to res, return 
        2. if start_index > length of digits, return 
        3. iterate over string of digits[start_index], with l
            1. add l to cur_comb 
            2. call the function again, with start_index + 1 
            3. cur_comb.pop()
    4. return res
    """
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = [] 
        self.dfs(digits, num_letters, res, 0, [])
        return res 
    
    def dfs(self, digits, num_letters, res, start_index, cur_comb):
        if len(cur_comb) == len(digits):
            res.append("".join(cur_comb))
            return 
        
        if start_index > len(digits):
            return
        
        for l in num_letters[digits[start_index]]:
            cur_comb.append(l) 
            self.dfs(digits, num_letters, res, start_index + 1, cur_comb)
            cur_comb.pop() 




