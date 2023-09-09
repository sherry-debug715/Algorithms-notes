"""
Description
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.

Lintcode problem 138: https://www.lintcode.com/problem/138/?fromId=161&_from=collection
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    """
    Key Logic:
             i
    A = [-3, 1, 2, -3, 4]
                    j
    to calculate the sum between i and j, sum[j] - sum[i], therefore, 
    if sum[j] == sum[i]
    we know, sum[i + 1:j] == 0
    """
    """
    Initialize a hash map, {0: -1}, name hash_map, key: current sum, value: index.
    Initialize a Integer, cur_sum, set it to 0
    Iterate over nums list with i:
        cur_sum += nums[i]
        check if cur_sum is in hash_map:
            return [ hash_map[cur_sum] + 1, i ] 
        hash_map[cur_sum] = i 
    """
    def subarray_sum(self, nums: List[int]) -> List[int]:
        hash_map = {0: -1}
        cur_sum = 0 

        for i in range(len(nums)): 
            cur_sum += nums[i]
            if cur_sum in hash_map:
                return [hash_map[cur_sum] + 1, i]
            hash_map[cur_sum] = i