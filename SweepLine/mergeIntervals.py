# Lintcode problem 156: https://www.lintcode.com/problem/156/?showListFe=true&page=1&problemTypeId=2&tagIds=389&ordering=level&pageSize=50

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return [] 
        intervals = sorted(intervals, key=lambda x: x.start)
        stack = []
        for cur in intervals:
            if not stack or cur.start > stack[-1].end:
                stack.append(cur)
                continue 
            prev = stack[-1] 
            prev.end = max(prev.end, cur.end)
        
        return stack 
