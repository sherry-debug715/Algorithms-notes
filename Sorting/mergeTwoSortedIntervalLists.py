# Lintcode problem 839: https://www.lintcode.com/problem/839/

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
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    # Time: O(N)
    # Space: O(N)
    def merge_two_interval(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        p1, p2 = 0, 0
        intervals = []
        while p1 < len(list1) and p2 < len(list2):
            if list1[p1].start < list2[p2].start:
                self.push_back(intervals, list1[p1])
                p1 += 1 
            else:
                self.push_back(intervals, list2[p2])
                p2 += 1 

        while p1 < len(list1):
            self.push_back(intervals, list1[p1])
            p1 += 1 
        while p2 < len(list2):
            self.push_back(intervals, list2[p2])
            p2 += 1
        
        return intervals 
    
    def push_back(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return 

        prev = intervals[-1]
        if interval.start > prev.end:
            intervals.append(interval)
            return
        if interval.start < prev.start and interval.end >= prev.start:
            prev.start = interval.start 
        if interval.start <= prev.end and interval.end > prev.end:
            prev.end = interval.end 
        

