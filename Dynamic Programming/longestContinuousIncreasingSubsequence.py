# Lintcode problem 397: https://www.lintcode.com/problem/397/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    """
    Time: O(N)
    Space: O(1)
    由于本题要求寻找的序列必须是连续的，所以只需用两个变量来记录每一次严格单增或者严格单减的序列长度并记录下最大值即可。
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        if not a:
            return 0 

        increase = 1
        decrease = 1
        output = 1

        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                decrease = 1
                increase += 1
                output = max(output, increase)
            elif a[i] < a[i - 1]:
                increase = 1
                decrease += 1
                output = max(output, decrease)

        return output 
            

