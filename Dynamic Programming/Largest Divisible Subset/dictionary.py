# Lintcode problem 603: https://www.lintcode.com/problem/603/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        # dp[n] references the amount of elements from nums that satisfy the requirement
        # till n.
        dp = {}
        # prev[n] references the prev number of n, in which, n is one of the element from
        # the longest subset that meets the requirement. 
        prev = {} 
        lastOfLongest = nums[0] 
        nums.sort()

        for n in nums:
            dp[n] = 1
            prev[n] = -1 
        
        for n in nums:
            for factor in self.get_factors(n):
                if factor not in dp:
                    continue 
                if dp[n] < dp[factor] + 1:
                    dp[n] = dp[factor] + 1
                    prev[n] = factor 
            
            if dp[lastOfLongest] < dp[n]:
                lastOfLongest = n 
        
        return self.get_result(prev, lastOfLongest) 
    
    def get_factors(self, num):
        if num == 1:
            return []
        factors = [] 
        cur_f = 1

        while cur_f * cur_f <= num:
            if num % cur_f == 0:
                factors.append(cur_f) 
                if cur_f * cur_f != num and cur_f != 1:
                    factors.append(num // cur_f) 
            cur_f += 1 
        
        return factors
    
    def get_result(self, prev, lastOfLongest):
        output = []
        while lastOfLongest != -1:
            output.append(lastOfLongest)
            lastOfLongest = prev[lastOfLongest] 
        return output[::-1] 