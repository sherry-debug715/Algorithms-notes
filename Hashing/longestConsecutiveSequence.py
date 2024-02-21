# Lintcode problem 124: https://www.lintcode.com/problem/124/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    """
        Edge case:
            if num is empty:
                return 0 
        Code:
            create a set, storage, for constant look up time.
            initialize a max_count, set it to float("-inf")
            Iterate over num, for each number:
                initialize a cur_count, set it to 0
                check if num is the start of a sequence by checking num - 1 not in set: 
                    curNum = num
                    while curNum exist in storage:
                        cur_count += 1
                        curNum += 1
                    max_count = max(max_count, cur_count)
                    set cur_count to 0 
            return max_count
                    
    """
    # Time: O(N)
    # Space: O(N)
    def longest_consecutive(self, num: List[int]) -> int:
        if not num:
            return 0 
        
        storage = set(num)
        max_count = float("-inf")
        for n in num:
            if n - 1 in storage:
                continue 
            cur_count = 1
            while n + cur_count in storage:
                cur_count += 1
            
            max_count = max(max_count, cur_count)
        
        return max_count
