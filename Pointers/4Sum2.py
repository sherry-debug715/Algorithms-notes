# Lintcode problem 976: https://www.lintcode.com/problem/976/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param a: a list
    @param b: a list
    @param c: a list
    @param d: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def four_sum_count(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        counter = {}
        output = 0
        for n1 in a:
            for n2 in b:
                two_sum = n1 + n2
                counter[two_sum] = counter.get(two_sum, 0) + 1

        for n3 in c:
            for n4 in d:
                two_diff = -(n3 + n4) 
                if two_diff in counter:
                    output += counter.get(two_diff, 0)

        return output  
