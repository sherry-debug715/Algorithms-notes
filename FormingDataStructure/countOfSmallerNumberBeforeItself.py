"""
Lintcode problem 249: https://www.lintcode.com/problem/249/
"""
from typing import (
    List,
)

class Block:
    def __init__(self):
        self.total = 0
        self.values = {} 

class BlockArr:
    def __init__(self, value):
        # value // 100 + 1 so we include 0 
        self.blocks = [
            Block() for _ in range(value // 100 + 1)
        ] 
    
    def count_smaller(self, num):
        # calculate it's block 
        block_idx = num // 100
        count = 0
        for i in range(block_idx):
            count += self.blocks[i].total 
        
        cur_block_values = self.blocks[block_idx].values
        for v in cur_block_values:
            if v < num:
                count += cur_block_values[v]
        
        return count 
    
    def insert(self, num):
        # calculate it's block
        block_idx = num // 100 
        block = self.blocks[block_idx]
        block.total += 1 
        block.values[num] = block.values.get(num, 0) + 1

class Solution:
    """
    @param a: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def count_of_smaller_number_i_i(self, a: List[int]) -> List[int]:
        if not a:
            return []

        block = BlockArr(10000)
        output = [] 
        for n in a:
            count = block.count_smaller(n) 
            output.append(count) 
            block.insert(n) 
        
        return output 
