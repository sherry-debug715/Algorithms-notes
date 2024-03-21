# Lintcode problem 382: https://www.lintcode.com/problem/382/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param s: A list of integers
    @return: An integer
              m      
s = [2, 3, 4, 5, 6, 7]
     l     
                 r
output = 1 + 2 + 

if s[l] + s[m] > s[r], it means any number between s[l] and s[m], inclusive, when 
paired with s[m] is greater than s[r]
    """
    def triangle_count(self, s: List[int]) -> int:
        if not s:
            return 0

        s.sort()
        output = 0
        n = len(s) 
        for r in range(2, len(s)):
            l, m = 0, r - 1
            while l < m:
                if s[l] + s[m] > s[r]:
                    output += (m - l)
                    m -= 1
                else:
                    l += 1
        
        return output 