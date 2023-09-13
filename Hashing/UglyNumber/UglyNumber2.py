"""
Lintcode problem 4: https://www.lintcode.com/problem/4/?fromId=161&_from=collection
"""

import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    """
    If n <= 0:
        return -1 

    Initialize a list, prime_factors, populated with 2, 3, 5 
    Initialize a hash set, visited
    Add 1 to visited
    Initialize a min heap, ugly.
    Add 1 to min heap
    Initialize a number, cur_ugly, set it to 1

    For n times:
        reassign cur_ugly to the current smallest number from ugly
        Iterate over prime_factors, with n:
            Initialize a number, next_ugly, set it to cur_ugly * n 
            If next_ugly is not in visited:
                add it to visited
                add it to ugly 

    return cur_ugly
    """

# Time: O(nLogn)
# Space: O(n)
    def nth_ugly_number(self, n: int) -> int:
        if n <= 0:
            return -1 
        
        prime_factors = [2, 3, 5] 
        visited = set([1]) 
        ugly = [1]
        heapq.heapify(ugly) 
        cur_ugly = 1 

        for _ in range(n):
            cur_ugly = heapq.heappop(ugly) 
            for n in prime_factors:
                next_ugly = n * cur_ugly 
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(ugly, next_ugly) 
        
        return cur_ugly 